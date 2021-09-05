from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def import_packages():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    import pandas as pd

def start_driver(driver):
    driver = webdriver.Chrome('./chromedriver') 
    return driver

def reset_variable(input):
    
    if type(input) == str:
        input = ''
    if type(input) == int:
        input = 0
    if type(input) == list:
        input = []
    if type(input) == bool:
        input = False
    return input


def create_dict(*args):
      return dict({i:eval(i) for i in args})

def seperate_month_and_year(month_and_year):
    year, month = month_and_year
    dummy_list = [year, month]
    return dummy_list