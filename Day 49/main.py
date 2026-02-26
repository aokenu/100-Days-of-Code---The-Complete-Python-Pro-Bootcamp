from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeDrivers()
chrome_options.add_experimental_option("detach", True)


# creating an instance of the driver
driver = webdriver.Chrome(option=chrome_options)
driver.get(URL)
