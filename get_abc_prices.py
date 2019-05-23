import os
import sys

from simple_settings import settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

CHROMEDRIVER_PATH = '%s/chromedriver' % os.path.dirname(os.path.realpath(__file__))

def get_price_json():

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    browser.get(('https://www.abc.virginia.gov/products'))

    search = browser.find_element_by_css_selector('input[form="coveo-dummy-form"]:nth-child(3)')
    search.send_keys('bourbon')

    search_button = browser.find_element_by_css_selector('a[data-qe-id="product-search-btn"]')
    search_button.click()

get_price_json()