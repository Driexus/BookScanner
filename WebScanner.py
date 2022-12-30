# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 14:50:01 2022

@author: Dimitris
"""

import pyautogui
import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, headless):
        opts = Options()
        if headless:
            opts.add_argument("--headless")
        
        self.browser = Firefox(options=opts)
        self.wait = WebDriverWait(self.browser, 10)
    
    def translate_image(self, path):
        self.browser.get("https://www.google.gr/?hl=en")        
        
        accept_button = self. browser.find_element('id', 'L2AGLb')
        accept_button.click()
        
        image_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]')))
        image_button.click()
        
        upload_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/c-wiz/div[2]/div/div[3]/div[2]/div/div[2]/span')))
        upload_button.click()
        
        pyautogui.write(r'C:\Users\Dimitris\Desktop\BookScanner\spanish.png')
        time.sleep(1)
        pyautogui.press('return')
        
        cookie_reject_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button')))
        cookie_reject_button.click()
        
        time.sleep(7)
        translate_button = self.wait.until(EC.element_to_be_clickable((By.ID, "ucj-5")))
        translate_button.click()
        
        time.sleep(5)
        
        translation_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/c-wiz/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div[3]')))
        text = translation_section.text
        
        print(text)

browser = Browser(False)
browser.translate_image("")