from selenium import webdriver

import tkinter as tk
from tkinter import ttk

from app import *

def search_item_func():
    chrome = webdriver.Chrome(executable_path="/Users/ulaganathan/Software/ChromeDriver/chromedriver")
    chrome.get("https://www.flipkart.com/")

    element = chrome.find_element_by_name("q")
    element.send_keys(search_item)


frame = tk.Tk()
frame.title("Web Scraping")

website = tk.StringVar()
search_item = tk.StringVar()

welcome = tk.Label(frame, text="Welcome to Web Scraping", fg="red").grid(row=0, column=0)

website_label = tk.Label(frame, text= "Websites").grid(row=2, column=0)
websites_avalabile = ttk.Combobox(frame, textvariable=website, values= ["Flipkart"], state= "readonly").grid(row=2, column=1)

info_label = tk.Label(frame, text='Type below like "Laptop" to search for it in the Website', fg="red").grid(row=3, column=0)

search_item_label = tk.Label(frame, text= "Search Item").grid(row=4, column=0)
search_item_entry = tk.Entry(frame, textvariable=search_item).grid(row=4, column=1)

search_button = tk.Button(frame, text= "Search", fg= "blue", command= search_item_func).grid(row=6, column= 0)

frame.mainloop()




#
# user_choice = """
# Enter :
# - 'h' to know the commands
# - 'a' to list all the Laptops
# - 'b' to list the best Laptops
# - 'c' to list the cheapest Laptops
# - 'q' to quit
#
# """
# print(user_choice)
#
# user_input = input("Enter Here : ")
# user_input = user_input.strip().lower()
#
# while user_input != 'q':
#     if user_input == 'h':
#         print(user_choice)
#     elif user_input == 'a':
#         all_laptops()
#     elif user_input == 'b':
#         best_laptops()
#     elif user_input == 'c':
#         cheapest_laptops()
#     else:
#         print("Wrong Command")
#
#     user_input = input("Enter Here : ")
#     user_input = user_input.strip().lower()