from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


URL = "https://www.python.org/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


event_dict = {} # create an empty list
events = number_of_event = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li') # get the total number of all the events

# loop over the total events to extact each event and date
for index, event in enumerate(events, start=0):
    time_el = event.find_element(By.TAG_NAME, 'time').text # looks inside that <li> for the first <time> child element and returns another WebElement.
    name_el = event.find_element(By.TAG_NAME, 'a').text # looks inside that <li> for the first <time> child element and returns another WebElement.

    # add each of the events,date to the event_dict
    event_dict[index] = {
            "time": time_el,
            "name": name_el
            }   


print(event_dict)




driver.quit()