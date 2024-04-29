# pre-requisites
# pip install selenium => install
# pip show selenium    => check if installed
# 4.17.2 here
# requires external installation of chromedriver if < selenium 4.6

from selenium import webdriver

# sends keyboard commands | fills out input
from selenium.webdriver.common.keys import Keys

# convinient finders/ locators
from selenium.webdriver.common.by import By

# for explicit waits with condition
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# sensative data  '.env' => not commitable
from dotenv import dotenv_values

config = dotenv_values('.env')

# High level Automation flow
# - Verify that the user is logged in ParentSquare (with valid credantials)
# - Verify that the user is placed on 'Allerts and Notices' tab

# selectors & assert data
TITTLE = 'Sign In | ParentSquare'
LOGIN_FLD = '#session_email'
PASS_FLD = '#session_password'
SIGNIN_BTN = 'input.btn:nth-child(4)'

SEARCH_BAR = '#query'
# absolute path
ALERT_TAB = 'ul.side-menu:nth-child(3) > li:nth-child(3) > a:nth-child(1)'

NOTICE_BTN = '#notice_type_all'

ALERT_HEADER = '.header-text > h2:nth-child(1)'
ALERT_TXT = 'Alerts and Notices'

# Test Flow
driver = webdriver.Chrome()
driver.get(config['LOGIN_URL'])

# check title
page_title = driver.title
assert page_title == TITTLE

# implicit wait 2sec
driver.implicitly_wait(2)

# fill in credentials
login_input = driver.find_element(By.CSS_SELECTOR, LOGIN_FLD)
login_input.send_keys(config['LOGIN'])
pass_input = driver.find_element(By.CSS_SELECTOR, PASS_FLD)
pass_input.send_keys(config['PASS'])
# submit
signin_btn = driver.find_element(By.CSS_SELECTOR, SIGNIN_BTN)
signin_btn.send_keys(Keys.RETURN)

# init explicit waits with 5 sec timecap
wait = WebDriverWait(driver, 5)

## Main page valdiation
# Err if waits fail
search_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SEARCH_BAR)))
alert_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ALERT_TAB)))
alert_tab.click()

# Alert Page validation 
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, NOTICE_BTN)))
alert_header = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ALERT_HEADER)))

assert alert_header.text == ALERT_TXT

driver.quit()
