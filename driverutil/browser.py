from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    """
    This class gets the browser name provided as an argument and creates the necessary driver.
    Additionally, it installs the needed webdriver for the selected browser.

    Args:
        browsername: the name of the browser for which the driver will be created

    Returns:
        a reference to the driver object that is created
    """

    def __init__(self):
        self.driver = None

    def get_browser(self, browsername):

        if browsername == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browsername == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        return self.driver
