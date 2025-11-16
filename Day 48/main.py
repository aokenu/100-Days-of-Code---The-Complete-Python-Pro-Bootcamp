from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD"

URL = "https://www.python.org/"

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


# finding elements by name
get_input = driver.find_element(By.NAME, value="q")
print(get_input.text)


# close the entire program
driver.quit()