#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 08:03:27 2022

@author: priteshsrivastava
"""

# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas

excel_data = pandas.read_excel(r'/Users/priteshsrivastava/Downloads/Recipients_data_1.xlsx', sheet_name='Recipients')
#print(excel_data['Contact'][0]+1)
count = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + 'Hi ' + str(excel_data['Name'][count]) + ' ji, ' + '\n' +  excel_data['Message'][0]
        print(url)
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
#            driver.findElement(By.cssSelector("span[data-icon='clip']")).click();
#            #add file to send by file path
#            driver.findElement(By.cssSelector("input[type='file']")).sendKeys(r'Users/priteshsrivastava/sddefault.jpeg');
#            #click to send
#            driver.findElement(By.cssSelector("span[data-icon='send-light']")).click();
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
#            attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
#            attachment_box.click()
#            image_box = driver.find_element_by_xpath(
#                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
#            image_box.send_keys(r'Users/priteshsrivastava/sddefault.jpeg')
            print(click_btn)
        except Exception as e:
            print(count)
            print("Sorry message could not sent to " + str(excel_data['Contact'][count]))
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(excel_data['Contact'][count]))
        count = count + 1
    except Exception as e:
        print(url)
        print(count)
        print('Failed to send message to ' + str(excel_data['Contact'][count] + str(e)))
        
driver.quit()
print("The script executed successfully.")