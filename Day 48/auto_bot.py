from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


URL = "https://orteil.dashnet.org/cookieclicker/"


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


select_lang = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
# select the "English" button from the langaage menu

print(select_lang.text)






# driver.quit()