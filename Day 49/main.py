from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

ACCOUNT_EMAIL = "datadotng@gmail.com" 
ACCOUNT_PASSWORD = "NP7tZsYipA5XRGC"
GYM_URL = "https://appbrewery.github.io/gym/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)


# create a user profile for chrome
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# launch the browser
driver.get(GYM_URL)

user_login = driver.find_element(By.ID, value="login-button")