from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://youtube.com/')

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
searchbox.send_keys('corey schafere selenium')

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()

time.sleep(2)
driver.quit()

# ===================================== Screenshot in .png to cwd
# file = driver.get_screenshot_as_png()
# with open('file.png', 'wb') as f:
#     f.write(file)

