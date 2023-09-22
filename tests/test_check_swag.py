from conftest import browser
from pages.swag_labs import SwagLabs

def test_check_elements_icon(browser):
    page_sauce_demo = SwagLabs(browser)
    page_sauce_demo.visit()
    assert page_sauce_demo.exist_icon()


def test_1_check_elements_user_name(browser):
    page_sauce_demo = SwagLabs(browser)
    page_sauce_demo.visit()
    assert page_sauce_demo.find_element('#user-name')

def test_2_check_elements_password(browser):
    page_sauce_demo = SwagLabs(browser)
    page_sauce_demo.visit()
    assert page_sauce_demo.find_element('#password')

