import customtkinter as ctk
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import main

title = 'Google Ads - Data Collector'

def get_categories(cat_loc):
        
        with webdriver.Firefox() as driver:
            
            driver.get("https://adsense.google.com/start/#calculator")
            
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[1]/div/button").click()
            
            # Selection int variable
            option = cat_loc
            
            # 1 - North America
            # 2 - South America
            # 3 - Europe, Middle East and Africa
            # 4 - Asia and Pacific countries
            
            driver.find_element(By.XPATH, f"/html/body/main/section[6]/div/div[2]/div/div[1]/div/div/ul/li[{option}]/button").click()
            
            driver.find_element(By.XPATH, "/html/body/main/section[6]/div/div[2]/div/div[2]/div/button").click()

            categories = []
            
            next_li = True
            i = 1
            
            while next_li:
                try:
                    li = driver.find_element(By.XPATH, f'/html/body/main/section[6]/div/div[2]/div/div[2]/div/div/ul/li[{i}]').text
                    categories.append(li)
                    i += 1
                except NoSuchElementException:
                    next_li = False
            
            print(categories)
            return categories

def open_screen():
    open_screen = ctk.CTkToplevel(window)
    open_screen.geometry("600x410")
    open_screen.title(title)

window = ctk.CTk()
window._set_appearance_mode("system")
window.title(title)
window.geometry("800x450")
window.resizable(width=False, height=False)
window.wm_iconbitmap("img/icon.ico")
ctk.set_default_color_theme("styles/dark-purple.json")

frame_l = ctk.CTkFrame(master=window, width=370, height=266).place(x=10, y=126)

frame_r = ctk.CTkScrollableFrame(window, label_anchor='w', orientation='vertical', width=370, height=255)
frame_r.place(x=395, y=125)

categories = ['Artes e entretenimento', 'Automóveis e veículos', 'Casa e jardim', 'Ciência', 'Comidas e bebidas', 'Compras', 'Computadores e aparelhos eletrônicos', 'Comunidades on-line', 'Comércio e indústrias', 'Condicionamento físico e beleza', 'Empregos e educação', 'Esportes', 'Finanças', 'Hobbies e lazer', 'Imóveis', 'Internet e telecomunicações', 'Jogos', 'Lei e governo', 'Livros e literatura', 'Notícias', 'Pessoas e sociedade', 'Pets e animais', 'Referência', 'Saúde', 'Viagem']


i = 0
for row in categories:
    cat_cbx = ctk.CTkCheckBox(frame_r, text=f"{row}", font=('Calibri', 16), bg_color='transparent', onvalue="on", offvalue="off")
    cat_cbx.pack(anchor='w', pady=8, padx=20)
    cat_cbx.select()
    i += 1


title = ctk.CTkLabel(master=window, text=title, font=("Calibri", 28, 'bold'))
title.pack(ipady=30)
subtitle_l = ctk.CTkLabel(master=window, text="Location", bg_color='transparent', font=("Calibri", 17, 'bold'), width=65, height=20).place(x=160, y=100)
subtitle_r = ctk.CTkLabel(master=window, text="Category", bg_color='transparent', font=("Calibri", 17, 'bold'), width=65, height=20).place(x=550, y=100)


rad_var = ctk.IntVar(value=0)

na_rad_btn = ctk.CTkRadioButton(master=frame_l, value=1, variable=rad_var, text="North America", bg_color='transparent', font=('Calibri', 16), width=100, height=10).place(x=40, y=150)
sa_rad_btn = ctk.CTkRadioButton(master=frame_l, value=2, variable=rad_var, text="South America", bg_color='transparent', font=('Calibri', 16), width=100, height=10).place(x=40, y=185)
eur_rad_btn = ctk.CTkRadioButton(master=frame_l, value=3, variable=rad_var, text="Europe, Middle East and Africa", bg_color='transparent', font=('Calibri', 16), width=100, height=10).place(x=40, y=220)
asn_rad_btn = ctk.CTkRadioButton(master=frame_l, value=4, variable=rad_var, text="Asia and Pacific countries", bg_color='transparent', font=('Calibri', 16), width=100, height=10).place(x=40, y=255)


def confirm_options():
    loc = rad_var.get()
    cat = 5
            
    print(f'loc: {loc}, cat: {cat}')
    main.DataCollector.get_data(loc, cat)
    


btn_confirm = ctk.CTkButton(master=window, text="Confirm", command=confirm_options, font=("Calibri", 18), width=70, height=30).place(x=350, y=405)

    
window.mainloop()

