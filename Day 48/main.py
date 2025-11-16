from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")


# close the browser
driver.close()

# close the entire program
driver.quit()