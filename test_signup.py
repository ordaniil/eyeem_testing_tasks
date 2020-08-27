import unittest
import argparse
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import actions as act
from values.strings import *
from driverutil.browser import Browser


class TestSignup(unittest.TestCase):
    """
    This test checks the sign up flow of a buyer on https://www.eyeem.com/

    usage: test_signup.py [-h] [-b BROWSER]

    optional arguments:
        -h, --help
            show this help message and exit
        -b BROWSER, --browser BROWSER
            name of the browser
    """

    def setUp(self):
        self.driver = Browser().get_browser(browsername)
        self.driver.get(BASE_URL)

    def test_signup(self):
        # Click on initial signup button
        act.find_and_click(self.driver,X_SIGNUP_BUTTON_INIT)
        time.sleep(2)

        # Click on "For Image Buyers" button
        act.find_and_click(self.driver,X_BUYER_BUTTON)
        time.sleep(2)

        # Fill user's email
        act.enter_text(self.driver,X_EMAIL,EMAIL)
        time.sleep(2)

        # Fill user's password
        act.enter_text(self.driver,X_PASSWORD,PASSWORD)
        time.sleep(2)

        # Click on signup button
        act.find_and_click(self.driver,X_SIGNUP)
        time.sleep(2)

        ### VERIFICATION ###
        # Click on Account button
        act.find_and_click(self.driver,X_ACCOUNT)
        time.sleep(2)

        # Click on Settings button
        act.find_and_click(self.driver,X_SETTINGS)
        time.sleep(2)

        # Validate the Email field exists
        act.validate_field(self.driver,X_ASSERT_EMAIL)
        time.sleep(2)

        # Validate the user's Email is in the Email field
        act.verify_text_content(self.driver,X_ASSERT_EMAIL,EMAIL)
        time.sleep(2)

        # Click on Settings button
        act.find_and_click(self.driver,X_ACCOUNT)
        time.sleep(2)

        # Log out
        act.find_and_click(self.driver,X_LOGOUT_BUTTON)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    browser = argparse.ArgumentParser()
    browser.add_argument("-b", "--browser", required=False,
                        help="name of the browser", default="chrome")
    browser.add_argument('unittest_args', nargs='*')
    args = browser.parse_args()
    sys.argv[1:] = args.unittest_args
    browsername = vars(args)["browser"]
    unittest.main()
