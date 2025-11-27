from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


URL = "https://orteil.dashnet.org/cookieclicker/"


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# this time will make surethe website loads completely with the language selection before proceeding to the next line of code
time.sleep(5)

select_lang = driver.find_element(By.ID, value='langSelect-EN')


# select the "English" button from the langaage menu
select_lang.click()

time.sleep(10)

# click the captcha
checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="GjRM0"]/div/label/input'))
)
checkbox.click()



# driver.quit()