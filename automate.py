from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import WEBDRIVER_PATH
from register import test_registration  # Importing the registration function
from fundCampaign import fund_campaign
from login import login  # Importing the login function

def initialize_webdriver():
    service = Service(executable_path=WEBDRIVER_PATH)
    driver = webdriver.Chrome(service=service)  # Initialize WebDriver
    return driver

def automate():
    # Initialize WebDriver
    driver = initialize_webdriver()

    try:
        # Perform Registration
        test_registration(driver)

        # Perform Login after Registration
        login(driver)


        fund_campaign(driver)

    finally:
        # Close the driver after the process
        driver.quit()

if __name__ == "__main__":
    automate()
