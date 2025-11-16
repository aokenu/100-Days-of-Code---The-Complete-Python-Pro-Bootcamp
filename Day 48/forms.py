from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



URL = "https://secure-retreat-92358.herokuapp.com/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


# enter first name in form field for first name
field_1 = driver.find_element(By.NAME, value="fName")
field_1.send_keys("Austine")
time.sleep(2)

# enter last name in form field for last name
field_2 = driver.find_element(By.NAME, value="lName")
field_2.send_keys("Doe")
time.sleep(2)

# enter email in form field for email address
field_2 = driver.find_element(By.NAME, value="email")
field_2.send_keys("goldstine86@gmail.com")
time.sleep(2)

# click the submit button
submit = driver.find_element(By.TAG_NAME, value="button")
submit.click()
time.sleep(2)



driver.quit()