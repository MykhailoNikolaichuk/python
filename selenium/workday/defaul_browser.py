from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(r'--user-data-dir=C:\Users\mykhailo.nikolaichu\AppData\Local\Google\Chrome\User Data\Default') # change to profile path
chrome_options.add_argument(r'--profile-directory=Profile 1')

browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe", chrome_options=chrome_options) # change the executable_path too
browser.maximize_window()
'''
It work some how, but not in a way that I want
'''