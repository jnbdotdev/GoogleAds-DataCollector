import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import cv2
import pytesseract
import pyscreenshot as ImageGrab
import preprocessing

class DataCollector:
    # Path to Tesseract executable
    TESSERACT_CMD = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract.exe'
    # Path to save screenshots
    IMG_PATH = "img/screenshot.jpg"
    # Custom configuration for Tesseract OCR
    CUSTOM_CONFIG = r'--oem 3 --psm 6'
    # List of category names for reference
    CATEGORIES = [
        'Arts and entertainment', 'Automobiles and vehicles', 'House and garden', 'Science',
        'Food and drinks', 'Shopping', 'Computers and electronic devices', 'Online communities',
        'Commerce and industries', 'Fitness and beauty', 'Jobs and education', 'Sports',
        'Finance', 'Hobbies and leisure', 'Properties', 'Internet and telecommunications',
        'Games', 'Law and government', 'Books and literature', 'News', 'People and society',
        'Pets and animals', 'Reference', 'Health', 'Trip'
    ]

    def __init__(self):
        # Initialize the DataCollector class and set up Tesseract
        print('Initializing DataCollector...')
        pytesseract.pytesseract.tesseract_cmd = self.TESSERACT_CMD

    def read_image(self, gscale):
        # Converts an image to grayscale using different color spaces and performs OCR
        grayscale_modes = [cv2.COLOR_BGR2Luv, cv2.COLOR_BGR2Lab, cv2.COLOR_BGR2XYZ]
        grayscale = grayscale_modes[gscale]
        print(f'Testing {["Luv", "Lab", "XYZ"][gscale]} scale')

        # Read the image from the saved path
        image = cv2.imread(self.IMG_PATH)
        gray = cv2.cvtColor(image, grayscale)
        noise = preprocessing.remove_noise(gray)
        canny = preprocessing.canny(noise)
        thresh = preprocessing.thresholding(canny)
        
        # Extract text from the processed image using Tesseract OCR
        text = pytesseract.image_to_string(thresh, config=self.CUSTOM_CONFIG)
        text = re.sub(r'\D', '', text)
        value = int(text) if text else 0

        # Retry with different grayscale modes if value is less than 1000
        if value < 1000 and gscale < 2:
            return self.read_image(gscale + 1)
        
        return [value, 'Success' if gscale == 0 else 'Reviewed']

    def image_scraping(self, result_row):
        # Capture a screenshot of the specific area where the result is displayed
        location = result_row.location
        size = result_row.size
        x1 = int(location['x'] + 60)
        x2 = int((location['x'] + size['width']) - 60)
        y1 = int(location['y'] - 1900)
        y2 = int((location['y'] - size['height']) - 1700)
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        image.save(self.IMG_PATH, 'jpeg')

def get_data(loc, cat):
    # Main function to collect data by interacting with the web page
    data_collector = DataCollector()
    with webdriver.Firefox() as driver:
        driver.get("https://adsense.google.com/start/#calculator")
        data = []

        for reg in loc:
            # Select the region
            driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[1]/div/button").click()
            driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[1]/div/div/ul/li[{reg}]/button").click()

            for second_option in cat:
                # Initialize list to store categories
                categories = []

                # Select the category
                driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[2]/div/button").click()
                category = driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[2]/div/div/ul/li[{second_option}]/button")
                categories.append(DataCollector.CATEGORIES[second_option - 1])
                category.click()
                
                # Calculate and display results
                driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/button").click()
                driver.execute_script("window.scrollTo(0, 2000)")
                time.sleep(1)  # Short pause for visualization

                # Scrape the result from the displayed area
                result_row = driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[3]/div[3]/div[1]")
                data_collector.image_scraping(result_row)
                driver.execute_script("window.scrollTo(0, 1500)")
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[3]/button").click()

                # Read the value from the image
                from_image = data_collector.read_image(0)
                text = from_image[0]
                attempts = from_image[1]
                value = int(text)

                # Map region index to region name
                region = ['North America', 'South America', 'Europe, Middle East and Africa', 'Asia and Pacific countries'][reg - 1]
                data.append([categories[-1], value, region, attempts])

    # Save collected data to a CSV file
    with open("data/info.csv", "wt", newline='', encoding='UTF-8') as archive:
        writer = csv.writer(archive, delimiter=";")
        writer.writerow(["Category", "Value", "Region", "Status"])
        writer.writerows(data)
