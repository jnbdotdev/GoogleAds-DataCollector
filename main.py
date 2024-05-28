
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import csv
import numpy as np

import pyscreenshot as ImageGrab

import cv2
import pytesseract
import preprocessing

import easygui

import re


class DataCollector():
  
    def __init__(self):
        print('init')
  
    def get_data(loc, cat):
                
        with webdriver.Firefox() as driver:
            
            driver.get("https://adsense.google.com/start/#calculator")
            
            driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[1]/div/button").click()
            
            # Selection int variable
            option = loc
            
            # 1 - North America
            # 2 - South America
            # 3 - Europe, Middle East and Africa
            # 4 - Asia and Pacific countries
            
            driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[1]/div/div/ul/li[{option}]/button").click()
                            
            categories = []
            values = []
            ad_loc = []
            
            for second_option in range(1, cat):

                # Select the second ComboBox
                driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[2]/div/button").click()

                # Select option in ComboBox
                category = driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[2]/div/div/ul/li[{second_option}]/button")
                
                # Category name extraction
                category_name = category.text
                categories.append(category_name)
                
                category.click()

                # Calculate
                driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/button").click()

                # Y 1500 = Calculator section
                # Y 2000 = Result view
                driver.execute_script("window.scrollTo(0, 2000)")

                result_row = driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[3]/div[3]/div[1]")
                location = result_row.location
                xl, yl = location['x'], location['y']

                size = result_row.size
                w, h = size['width'], size['height']

                x1 = int(xl+60)
                x2 = int((xl+w)-60)
                y1 = int(yl-1900)
                y2 = int((yl-h)-1700)

                print("Second collection")
                print(f"X1: {x1}, Y1: {y1}\nX2: {x2}, Y2: {y2}")
                image = ImageGrab.grab(bbox=(x1,y1,x2,y2))
                image.save('img/screenshot.jpg', 'jpeg')

                # Little pause for visualization
                sleep(1)
                if(second_option < cat):
                    # Scroll back
                    driver.execute_script("window.scrollTo(0, 1500)")
                    sleep(1)

                    driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[3]/button").click()
                
                image = cv2.imread("img/screenshot.jpg")
                custom_config = r'--oem 3 --psm 6'
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
                noise = preprocessing.remove_noise(gray)
                canny = preprocessing.canny(noise)
                thresh = preprocessing.thresholding(canny)
                convertion = thresh
                
                # COLOR_BGR2Luv > Alta porcentagem (20/25)

                pytesseract.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract.exe'
                text = pytesseract.image_to_string(convertion, config=custom_config)
                print(text)
                text = re.sub(r'\D','', text)
                
                value = int(text)
                values.append(value)
                
                ad_locate = ''
                match loc:
                    case 1:
                        ad_locate = 'North America'
                    case 2:
                        ad_locate = 'South America'
                    case 3:
                        ad_locate = 'Europe, Middle East and Africa'
                    case 4:
                        ad_locate = 'Asia and Pacific countries'
                ad_loc.append(ad_locate)
                
                
        data = []
        for i in range(len(categories)):
            data.append([categories[i], values[i], ad_loc[i]])
        print(data)

        with open("data/info.csv", "wt") as archive:
            writer = csv.writer(archive, delimiter=";")
            writer.writerow(["Category", "Value", "Location"])
            
            for row in data:
                writer.writerow(row)
        
    if __name__ == '__main__':
        cat = int(easygui.enterbox('How many categories do you want to analyze?'))
        get_data(2, cat+1)