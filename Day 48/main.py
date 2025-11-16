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



event_list = []
events = number_of_event = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
event_count = len(events)
# for event in events:
#     event_list.append(event.text)
    #print(event_list)
range_count = [number for number in range(event_count)]

all_events = [range_count]

print(range_count)
#print(event_count)




# finding the event date by xpath
# event_date = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')


# # finding the event name by xpath
# event_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')


# # print(f"'time': {event_date.text}, 'name': {event_name.text}")

# number_of_event = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')

# # for event in number_of_event:
# #     print(event.text)

driver.quit()