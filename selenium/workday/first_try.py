

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://wd3.myworkday.com/gameloft/d/home.htmld")
driver.maximize_window()


#wait and click on login button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="noImageRequiredForLoadTime"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/ul/li[1]'))).click()

#enter login and password & submit it
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userNameInput")))
username_input = driver.find_element_by_id('userNameInput')
username_input.send_keys(os.environ.get('USER_NAME'))

password_input = driver.find_element_by_id('passwordInput')
password_input.send_keys(os.environ.get('USER_PASS'))
password_input.submit()

#skip remember device
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-1o8kyg5-ButtonAsLink'))).click()

#review time
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wd-home-applets"]/li[2]'))).click()

#this week
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'wd-DropDownCommandButton-56$205593'))).click()

#open submit list-button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[2]/div[1]/div[1]"))).click()

#click on time by type option
time.sleep(1) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[1]/ul/li[3]"))).click()

#TODO: choose type of activity /  fill the forms with 8 hours / send / STOP BEFORE SUBMIT
# time.sleep(2) 
#press minus
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[1]/div/div/button"))).click()


#press plus
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div[1]/table/tbody/tr/td[1]/div/div/div[1]/div/div[1]/button"))).click()


#open text-field
time.sleep(1) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div/div/div/div/div[1]/input"))).click()
                                                                        

# #click on recent
time.sleep(1) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[1]"))).click()

# #click on 1 elem
time.sleep(1) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[1]"))).click()


# click on second textfield burger
time.sleep(1) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/div/div/div/div/span"))).click()

# path to OTT
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]"))).click()

#click on OTT
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[1]/div/div[2]/div/div[1]/div/div/div[8]/div/div/div[2]"))).click()

#textfields with hours monday - friday
for index in range (5, 10):
    cell_with_hours = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[{index}]/div/div/input')
    cell_with_hours.clear()
    cell_with_hours.send_keys('8')

#ok button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div[1]/section/div[2]/div[1]/div[1]/button[1]"))).click()



time.sleep(60) 
driver.quit()