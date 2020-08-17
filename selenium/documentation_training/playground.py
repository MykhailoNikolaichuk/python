from selenium.webdriver.common.keys import Keys
from selenium import webdriver
def dir_help(func):
    help(func)
    print('\n' * 2 + '#' * 150 + '\n' * 2)
    print(dir(func))


# dir_help(Keys)
