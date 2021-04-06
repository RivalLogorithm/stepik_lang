import pytest
from selenium import webdriver
import time

def test_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    btn = None
    try:
        btn = browser.find_element_by_css_selector("#add_to_basket_form button[type='submit']")
    finally:
        assert btn is not None, 'Button not found'