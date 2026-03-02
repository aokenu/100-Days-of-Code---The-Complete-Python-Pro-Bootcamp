from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

ACCOUNT_EMAIL = "austinepython@test.com" 
ACCOUNT_PASSWORD = "NP7tZsYipA5XRGC"
GYM_URL = "https://appbrewery.github.io/gym/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# create a user profile for chrome
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
x
# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)

# launch the browser
driver.get(GYM_URL)

# ----------------  Step 2 - Automated Login ----------------

# define the waiting duration
wait = WebDriverWait(driver, 2)

# click the login button
login_btn = wait.until(EC.element_to_be_clickable(By.ID, "login-button")
login_btn.click()


# enter user email
user_email = driver.find_element(By.ID, value="email-input")
user_email.send_keys(ACCOUNT_EMAIL)
time.sleep(2)

# enter user password
user_pass = driver.find_element(By.ID, value="password-input")
user_pass.send_keys(ACCOUNT_PASSWORD)
time.sleep(2)

submit_user = driver.find_element(By.ID, value="submit-button")
submit_user.click()


# book a gym session
bookings = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "book-button-spin-2026-03-10-1800"))
)
driver.execute_script("arguments[0].click();", bookings)     

# driver.quit()
