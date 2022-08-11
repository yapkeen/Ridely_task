from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://test-ask.ridely.com/home")
login_box = driver.find_element(by=By.ID, value="mat-input-0")
password_box = driver.find_element(by=By.ID, value="mat-input-1")
login_button = driver.find_element(by=By.CLASS_NAME, value="mat-button-wrapper")
login_box.send_keys("test-trainer@ridely.com")
password_box.send_keys("T3st!")
login_button.click()
login_button.click()

time.sleep(3)
reviews_box = driver.find_element(by=By.XPATH, value="//span[text()='Reviews']")
reviews_box.click()

waiting_for_user_tab = driver.find_element(by=By.XPATH,
                                           value="//mat-panel-description["
                                                 "text()=' Response sent to user. Waiting for user to accept. ']")
waiting_for_user_tab.click()

time.sleep(1)
see_more_button = waiting_for_user_tab.find_element(by=By.XPATH, value="//td[5]/button/span")
see_more_button.click()

time.sleep(2)
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(25))
response_form = driver.find_element(By.XPATH, "//div[3]/div/div/div")
response_form.send_keys(random_string)

time.sleep(1)
send_button = driver.find_element(by=By.XPATH, value="//div[2]/button[3]/span/mat-icon")
send_button.click()

time.sleep(2)
added_string_element = driver.find_element(by=By.XPATH, value="//div[contains( text(), '" + random_string + "')]")

print(added_string_element.is_displayed())
assert added_string_element.is_displayed()
