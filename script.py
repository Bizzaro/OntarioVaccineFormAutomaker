import os
import sys
from csv import reader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import OrderedDict

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def readParams(filename):
    with open(filename, newline='') as iris:
        # returning from 2nd row
        return list(reader(iris, delimiter=','))[1:]

params = readParams(sys.argv[1])

chromedriver_location = params[0][7]

driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10000)
driver.get('https://covid19.ontariohealth.ca/app-identity?viewId=9MYRZKKV92R7')

#Page 1
hcn_xpath = '//*[@id="hcn"]'
hcn_back_xpath = '//*[@id="scn"]'
vn_xpath = '//*[@id="vcode"]'
dob_xpath = '//*[@id="dob"]'
postal_code_xpath = '//*[@id="postal"]'
continue_button = '//*[@id="continue_button"]'
continue_to_vacine = '//*[@id="booking_button"]'


print(params[0][0])
driver.find_element_by_xpath(hcn_xpath).send_keys(params[0][0])
driver.find_element_by_xpath(vn_xpath).send_keys(params[0][1])
driver.find_element_by_xpath(hcn_back_xpath).send_keys(params[0][2])
driver.find_element_by_xpath(dob_xpath).send_keys(params[0][3])
driver.find_element_by_xpath(postal_code_xpath).send_keys(params[0][4])
driver.find_element_by_xpath(continue_button).click()

#sleep(1)
#Ensures that the script does not exit during the queue wait time. 
WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.ID, "booking_button")))
driver.find_element_by_xpath(continue_to_vacine).click()