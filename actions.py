from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_and_click(driver,xpath):
    """
    Finding a button by its xpath and clicking it

    Args:
        driver: the instance of WebDriver that is going to be used
        xpath: the xpath of the button on the page
    """

    validate_field(driver,xpath)
    _button = driver.find_element_by_xpath(xpath)
    _button.click()

def enter_text(driver,xpath,value):
    """
    Finding a text field and filling it

    Args:
        driver: the instance of WebDriver that is going to be used
        xpath: the xpath of the field on the page
        value: the value that is going to be insterted in the field
    """

    validate_field(driver,xpath)
    _textField = driver.find_element_by_xpath(xpath)
    _textField.send_keys(value)

def validate_field(driver,xpath):
    """
    Validating an element exists

    Args:
        driver: the instance of WebDriver that is going to be used
        xpath: the xpath of the element on the page
    """

    _verifyField = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def verify_text_content(driver,xpath,value):
    """
    Verifying the content of a text field

    Args:
        driver: the instance of WebDriver that is going to be used
        xpath: the xpath of the element on the page
        value: the content that is going to be asserted
    """

    validate_field(driver,xpath)
    _textContent = driver.find_element_by_xpath(xpath).get_attribute("value")
    assert _textContent == value
