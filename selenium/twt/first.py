import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("seleniugkghkm")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

print(driver.title)
time.sleep(5)

# driver.quit()