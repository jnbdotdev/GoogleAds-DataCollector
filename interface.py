import customtkinter as ctk
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import main

def get_categories(cat_loc):
    # Function to fetch categories from the website based on selected region
    with webdriver.Firefox() as driver:
        driver.get("https://adsense-google-com.translate.goog/intl/pt-BR_br/start/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en-USr")
        sleep(2)
        
        # Click on the necessary buttons to navigate and select the region
        driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[1]/div/button").click()
        driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[1]/div/div/ul/li[{cat_loc}]/button").click()
        driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[2]/div/button").click()

        categories = []
        i = 1
        
        # Loop to collect all category names
        while True:
            try:
                li = driver.find_element(By.XPATH, f'/html/body/main/section[6]/div/div[2]/div/div[2]/div/div/ul/li[{i}]').text
                categories.append(li)
                i += 1
            except NoSuchElementException:
                break

        return categories

def verify_cat_selection():
    # Function to get indices of selected categories
    selected_indices = [index + 1 for index, var in enumerate(cat_vars) if var.get()]
    return selected_indices

def verify_reg_selection():
    # Function to get indices of selected regions
    selected_indices = [index + 1 for index, reg_cbx in enumerate(reg_checkboxes) if reg_cbx.get()]
    return selected_indices

def toggle_select_all():
    # Function to select or deselect all category checkboxes
    select_all = select_all_var.get()
    for var in cat_vars:
        var.set(select_all)

def update_select_all():
    # Function to update the "Select All" checkbox based on individual category selections
    all_selected = all(var.get() for var in cat_vars)
    select_all_var.set(all_selected)

def confirm_options():
    # Function to confirm the selected options and pass them to the main data collection function
    reg_selection = verify_reg_selection()
    cat_selection = verify_cat_selection()
    main.get_data(reg_selection, cat_selection)

def create_gui():
    # Function to create the main GUI window and populate it with widgets
    window = ctk.CTk()
    window._set_appearance_mode("system")
    window.title('Google Ads - Data Collector')
    window.geometry("800x450")
    window.resizable(width=False, height=False)
    window.wm_iconbitmap("img/icon.ico")
    ctk.set_default_color_theme("styles/dark-purple.json")

    # Create scrollable frames for regions and categories
    frame_l = ctk.CTkScrollableFrame(window, label_anchor='w', orientation='vertical', width=365, height=255)
    frame_l.place(x=10, y=126)

    frame_r = ctk.CTkScrollableFrame(window, label_anchor='w', orientation='vertical', width=375, height=255)
    frame_r.place(x=395, y=125)

    global cat_vars, reg_checkboxes, select_all_var
    cat_vars = []
    reg_checkboxes = []

    # "Select All" checkbox for categories
    select_all_var = ctk.BooleanVar()
    select_all_cbx = ctk.CTkCheckBox(frame_r, text="Select All", font=('Calibri', 16, 'bold'), bg_color='transparent', variable=select_all_var, command=toggle_select_all)
    select_all_cbx.pack(anchor='w', pady=8, padx=20)

    # Create category checkboxes
    for cat in categories:
        cat_var = ctk.BooleanVar()
        cat_cbx = ctk.CTkCheckBox(frame_r, text=f"{cat}", font=('Calibri', 16), bg_color='transparent', variable=cat_var, command=update_select_all)
        cat_cbx.pack(anchor='w', pady=8, padx=20)
        cat_vars.append(cat_var)

    # Create region checkboxes
    for reg in regions:
        reg_cbx = ctk.CTkCheckBox(frame_l, text=f'{reg}', font=("Calibri", 16), bg_color='transparent')
        reg_cbx.pack(anchor='w', pady=8, padx=20)
        reg_checkboxes.append(reg_cbx)

    # Configure scrollbar width to 0 to hide it
    frame_l._scrollbar.configure(width=0)

    # Create title and subtitles
    ctk.CTkLabel(master=window, text='Google Ads - Data Collector', font=("Calibri", 28, 'bold')).pack(ipady=30)
    ctk.CTkLabel(master=window, text="Region", bg_color='transparent', font=("Calibri", 17, 'bold'), width=65, height=20).place(x=160, y=100)
    ctk.CTkLabel(master=window, text="Category", bg_color='transparent', font=("Calibri", 17, 'bold'), width=65, height=20).place(x=550, y=100)

    # Create confirm button
    ctk.CTkButton(master=window, text="Confirm", command=confirm_options, font=("Calibri", 18), width=80, height=30).place(x=345, y=405)

    window.mainloop()

if __name__ == "__main__":
    # Define categories and regions
    categories = ['Arts and entertainment', 'Automobiles and vehicles', 'House and garden', 'Science', 'Food and drinks', 'Shopping', 'Computers and electronic devices', 'Online communities', 'Commerce and industries', 'Fitness and beauty', 'Jobs and education', 'Sports', 'Finance', 'Hobbies and leisure', 'Properties', 'Internet and telecommunications', 'Games', 'Law and government', 'Books and literature', 'News', 'People and society', 'Pets and animals', 'Reference', 'Health', 'Trip']
    regions = ['North America', 'South America', 'Europe, Middle East and Africa', 'Asia and Pacific countries']
    create_gui()
