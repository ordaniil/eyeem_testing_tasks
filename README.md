# Selenium automated test - EyeEm Signup
An automated test using Selenium and Python to test the buyer signup flow on www.eyeem.com.

### File structure

    ├── driverutil                      
    │   └── browser.py        # Creates the driver for selected browser
    ├── values                
    │   └── strings.py        # Global string variables and paths for needed elements
    ├── actions.py            # All automated actions that will be performed
    └── test_signup.py        # Base class of the test

### Prerequisites - Tool versions used in testing
- **Python 3.8** - https://www.python.org/downloads/
- **Selenium 3.141.0** - https://selenium-python.readthedocs.io/installation.html

#### Tested browsers
- Google Chrome 85.0.4183.83 (64-bit)
- Mozilla Firefox 80.0 (64-bit)

### Execution
`python test_signup.py`
Usage: `test_signup.py [-h] [-b BROWSER]`
>Note: If browser is not "firefox" or "chrome", google chrome will be used by default
