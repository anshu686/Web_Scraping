# -------   Lead Generation LinkedIn profile  ------

import argparse, os, time
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from xlwt import Workbook, Formula, easyxf


def Main():


    parser = argparse.ArgumentParser()
    parser.add_argument("email", help='linkedin email')
    parser.add_argument('password', help='linkedin password')
    # parser.add_argument('keyword', help='Search word')

    args = parser.parse_args()
    driver = webdriver.Chrome()

    driver.get('https://www.linkedin.com/uas/login')
    time.sleep(random.uniform(6, 10))

    # ----- Linkedin Credentials -------

    emailElement = driver.find_element_by_id("session_key-login")
    emailElement.send_keys(args.email)
    passElement = driver.find_element_by_id('session_password-login')
    passElement.send_keys(args.password)
    passElement.submit()

    # time.sleep(random.uniform(6, 10))
    # searchElement = driver.find_element_by_id('main-search-box')
    # searchElement.send_keys(args.keyword)
    # searchElement.submit() //*[@id="contact-list-container"]/ul/li[1]/div[2]/h3/a

    time.sleep(random.uniform(10, 15))
    print('Cool Man... you did automated login')
    networkElement = driver.find_element_by_xpath('//*[@id="nav-link-network"]')
    networkElement.click()
    print("clicked Network")
    time.sleep(random.uniform(10, 15))
    connectElement = driver.find_element_by_xpath('//*[@id="network-sub-nav"]/li[1]/a')
    print('Found all profile path')
    connectElement.click()
    time.sleep(random.uniform(3, 5))
    res = driver.find_element_by_xpath('// *[ @ id = "contact-list-container"] / ul / li[4] / div[2] / h3 / a')
    Count =0
    # print('Profile %d') % Count
    res.click()
    # driver.find_element_by_id('//*[@id="contact-list-container"]')
    # plist

    # // *[ @ id = "contact-list-container"] / ul / li[3] / div[2] / h3 / a
    # // *[ @ id = "contact-list-container"] / ul / li[2] / div[2] / h3 / a
    # print('Profile %d clicked') % Count
    time.sleep(random.uniform(3, 5))

    # driver.maximize_window()

    Name1 = driver.find_element_by_xpath('//*[@id="name"]/h1/span/span')
    Name = Name1.get_attribute('innerHTML')

    print('Fetching Information of %s ...' % Name)
    time.sleep(random.uniform(3, 5))

    print('Name of this Asshole: %s' % Name)

    Linkedin_URL = driver.current_url
    print('Profile_URL : %s' % Linkedin_URL)

    contact_info = driver.find_element_by_xpath('//*[@id="contact-info-tab"]')
    contact_info.click()
    print('Clicked link to get Email_Details')

    email = driver.find_element_by_xpath('// *[ @ id = "email-view"] / ul / li / a')
    emailID = email.get_attribute('text')
    print('Email : %s' % emailID)

    Phone_detail = driver.find_element_by_xpath('// *[ @ id = "phone-view"] / ul / li')
    Phone = Phone_detail.get_attribute('innerHTML')
    print(Phone)

    print('started working on Excel')
    # ----------------------------------------------------------------------
    wb = Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet("Profiles")
    col_width = 256 * 20

    # ------- Styles --------

    style1 = easyxf(
        'pattern: pattern solid, fore_colour green;'
        'align: vertical center, horizontal center;'
    )

    style2 = easyxf(

        'align: vertical center, horizontal center;'
    )

    # ------ Heading-----

    sheet1.write_merge(0, 0, 0, 4, 'This is the data from my Linkedin Profile', style1)

    # -----First Row -------

    a = sheet1.write(1, 0, "Name", style2)
    b = sheet1.write(1, 1, "Linkedin_profile", style2)
    c = sheet1.write(1, 2, "Email", style2)
    d = sheet1.write(1, 3, "Phone", style2)

    # ---- Col_width-------

    for i in range(4):
        sheet1.col(i).width = col_width

    print('First row done')

    e = sheet1.write(2, 0, str(Name))
    f = sheet1.write(2, 1, str(Linkedin_URL))
    g = sheet1.write(2, 2, str(emailID))
    h = sheet1.write(2, 3, str(Phone))

    print('saving excel')
    print('Great job')

    wb.save("Linkedin_data.xls")


    driver.back()

    # for Count in range(Count, len(res)):
    #     try:
    #         plist = driver.find_element_by_xpath('// *[ @ class = "contact-item-view"]')
    #         print('Profile %d') % Count
    #         plist(Count).click()
    #         # driver.find_element_by_id('//*[@id="contact-list-container"]')
    #         # plist
    #         plist.click()
    #         print('Profile %d clicked') % Count
    #         time.sleep(random.uniform(3, 5))
    #
    #         driver.maximize_window()
    #
    #         contact_info = driver.find_element_by_xpath('//*[@id="contact-info-tab"]')
    #         contact_info.click()
    #         print('last click')
    #
    #         email = driver.find_element_by_xpath('// *[ @ id = "email-view"] / ul / li / a')
    #         print(email.get_attribute('text'))
    #         driver.back()
    #     except:
    #         print("some issues is there")
    #         continue;

    # Creation of Excel







    # time.sleep(random.uniform(6, 8))
    # res = driver.find_element_by_id("results")
    # print('result element found')

    # jList = driver.find_element_by_xpath('//*[@id="content-outlet"]/div/section[3]/div[2]/div/section[3]/div/ul/li[1]/div/div[1]/h2/a')
    # Count = 0
    # print("Count =0")
    # time.sleep(15)
    #
    # jList.click()
    # try:
    #     k = driver.find_element_by_id('apply-job-button')
    #     print('found')
    #     temp = driver.find_element_by_id('save-job-button')
    #     print('Save id found')
    #     SBText = driver.find_element_by_class_name('save-job-button-text')
    #     tempVal = SBText.text
    #     print('%s') % tempVal
    #     if tempVal == 'Save':
    #         temp = driver.find_element_by_id('save-job-button')
    #         temp.click()
    #         time.sleep(17)
    # except:
    #     print('Quick Apply not found')
    # driver.back()
    # time.sleep(18)
    #
    # # for Count in range(Count, len(jList)):
    # #     try:
    # #         item = driver.find_element_by_xpath('//*[@id="content-outlet"]/div/section[3]/div[2]/div/section[3]/div/ul/li[1]/div/div[1]/h2/a')
    # #         print('Job %d') % Count
    # #         item[Count].click()
    # #
    # #         try:
    # #             k = driver.find_element_by_id('apply-job-button')
    # #             print('found')
    # #             temp = driver.find_element_by_id('save-job-button')
    # #             print('Save id found')
    # #             SBText = driver.find_element_by_class_name('save-job-button-text')
    # #             tempVal = SBText.text
    # #             print('%s') % tempVal
    # #             if tempVal == 'Save':
    # #                 temp = driver.find_element_by_id('save-job-button')
    # #                 temp.click()
    # #                 time.sleep(17)
    # #         except:
    # #             print('Quick Apply not found')
    # #         driver.back()
    # #         time.sleep(18)
    # #     except:
    # #         print("some issues is there")
    # #         continue;
    # # print('worked perfectly')
    # # driver.close()


if __name__ == '__main__':
    Main()