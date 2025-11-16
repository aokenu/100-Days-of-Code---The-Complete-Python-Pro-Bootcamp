from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD"

# URL = "https://www.python.org/"

URL = "https://en.wikipedia.org/wiki/Main_Page"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# finding elements in the html content by class
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is {price_dollar.text}.{price_cents.text}")
 
# ===================================== OTHER WAYS OF FINDING ELEMENTS ======================

# # finding elements by name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# # finding elements by id
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# finding elements by css element
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)


# ================================ FINDING ELEMENTS BY XPATH ================================

# price_list = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span[2]/text()')
# print(price_list.text)

# finding elements by css element
# menu = driver.find_element(By.XPATH, value='//*[@id="container"]/li[8]/ul/li[1]/a')
# print(menu.text)


# click_link = driver.find_element(By.LINK_TEXT, value="Content portals")
# click_link.click()

# find the "Search" input by name
search = driver.find_element(By.NAME, value="search")

time.sleep(2)

# send the keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

time.sleep(2)

# close the entire program
driver.quit()