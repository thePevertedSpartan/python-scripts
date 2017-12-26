from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
# example option: add 'incognito' command line arg to options
# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='C:\Users\Mayankk\Downloads\chromedriver_win32\chromedriver')

# go to website of interest
browser.get("https://www.adultwork.com/Search.asp")
submit   = browser.find_element_by_link_text( "Continue")
submit.click()
country=browser.find_element_by_name("cboCountryID")
select=Select(country)
select.select_by_value('158')
alert = browser.switch_to_alert()
alert.accept()
country=browser.find_element_by_name("cboRegionID")
select=Select(country)
select.select_by_value('1')
country=browser.find_element_by_name("intAgeTo")
country.send_keys("26")
gender=browser.find_element_by_id("cbxGenderID_2")
gender.click()
country=browser.find_element_by_name("cboLastLoginSince")
select=Select(country)
select.select_by_value('M1')
