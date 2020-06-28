import json
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


'''FIREFOX TEST's'''
driver = webdriver.Firefox() #init
driver.get('http://hrtest.alycedev.com/')
driver.maximize_window()

# TEST 1: Business logic rule 1 - basket never can give more than 1 apple per minute

free_apples_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a') #reset basket
ActionChains(driver).click(free_apples_btn).perform()

status_test = "PASS - Basket never can give more than one apple per minute" #default result
timer = 0

while timer < 60: #1 minute
    grab_apple_button = driver.find_element_by_css_selector('button.grab-apple')
    grab_apple_button.click() #take from the basket
    number_of_lines = driver.find_elements_by_css_selector('div.col-12:nth-child(2) > ul > li') #check list

    if len(number_of_lines) > 1: #if there is more than one item in the list, then an error
        status_test = "FAILED - Basket can give more than one apple per minute"
        break

    timer += 1
    time.sleep(1)

print("TEST Firefox: Business logic rule №1 - ", status_test) #output result


'''TEST 2: Business logic rule №2'''
free_apples_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a') #reset basket
ActionChains(driver).click(free_apples_btn).perform()

while True: #empty the basket
    jonathan_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button') #click on the first button
    ActionChains(driver).click(jonathan_grab_apple).perform()

    adrian_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div[1]/span/button') #click on the second button
    ActionChains(driver).click(adrian_grab_apple).perform()

    julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button') #click on the third button
    ActionChains(driver).click(julia_grab_apple).perform()
    time.sleep(0.1) #pause

    if driver.find_elements_by_xpath("//div[contains(text(), 'Apple basket is empty')]"): #confirm that the basket is empty
        break

response = requests.get('http://hrtest.alycedev.com/users') #parse JSON
users_json = json.loads(response.text) #deserialization

for user in users_json: #extract id's
    id_apples_lists = user['apples']
    result_id = []
    for apples_dict in id_apples_lists:
        apple_id = apples_dict['id']
        result_id.append(apple_id) #create id's lists

    even_count = 0
    odd_count = 0
    for i in result_id: #distribute the values
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if even_count == 0 or odd_count == 0: #if the values ​​are of the same type - PASS
        status_test = "PASS - User never can have apples with both odd and even ids"
    else: #FAIL
        status_test = "FAILED - User can have apples with both odd and even ids"
        break

print("TEST Firefox: Business logic rule №2 - ", status_test) #output result
time.sleep(1)
driver.close()




# CHROME TEST's
driver = webdriver.Chrome("/Users/pushkavatrushka/PycharmProjects/hrtest-alycedev/chromedriver")
driver.get('http://hrtest.alycedev.com/')
driver.maximize_window()

# TEST 1: Business logic rule 1 - basket never can give more than 1 apple per minute

free_apples_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a') #reset basket
ActionChains(driver).click(free_apples_btn).perform()

status_test = "PASS - Basket never can give more than one apple per minute" #default result
timer = 0

while timer < 60: #1 minute
    grab_apple_button = driver.find_element_by_css_selector('button.grab-apple')
    grab_apple_button.click() #take from the basket
    number_of_lines = driver.find_elements_by_css_selector('div.col-12:nth-child(2) > ul > li') #check list

    if len(number_of_lines) > 1: #if there is more than one item in the list, then an error
        status_test = "FAILED - Basket can give more than one apple per minute"
        break

    timer += 1
    time.sleep(1)

print("TEST Firefox: Business logic rule №1 - ", status_test) #output result


'''TEST 2: Business logic rule №2'''
free_apples_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a') #reset basket
ActionChains(driver).click(free_apples_btn).perform()

while True: #empty the basket
    jonathan_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button') #click on the first button
    ActionChains(driver).click(jonathan_grab_apple).perform()

    adrian_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div[1]/span/button') #click on the second button
    ActionChains(driver).click(adrian_grab_apple).perform()

    julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button') #click on the third button
    ActionChains(driver).click(julia_grab_apple).perform()
    time.sleep(0.1) #pause

    if driver.find_elements_by_xpath("//div[contains(text(), 'Apple basket is empty')]"): #confirm that the basket is empty
        break

response = requests.get('http://hrtest.alycedev.com/users') #parse JSON
users_json = json.loads(response.text) #deserialization

for user in users_json: #extract id's
    id_apples_lists = user['apples']
    result_id = []
    for apples_dict in id_apples_lists:
        apple_id = apples_dict['id']
        result_id.append(apple_id) #create id's lists

    even_count = 0
    odd_count = 0
    for i in result_id: #distribute the values
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if even_count == 0 or odd_count == 0: #if the values ​​are of the same type - PASS
        status_test = "PASS - User never can have apples with both odd and even ids"
    else: #FAIL
        status_test = "FAILED - User can have apples with both odd and even ids"
        break

print("TEST Firefox: Business logic rule №2 - ", status_test) #output result
time.sleep(1)
driver.close()
