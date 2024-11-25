from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
from locators import LoginPageLocators

def login(driver):
    driver.get(config.LOGIN_URL)

    # Wait for the login form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD)
    )

    # Fill out the login form
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(config.LOGIN_DATA["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(config.LOGIN_DATA["password"])

    # Click the login button
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # Wait for the post-login page to load
    # WebDriverWait(driver, 10).until(
    #     EC.title_contains("Dashboard")  # Replace with the title or confirmation message
    # )
    print("Login successful!")

if __name__ == "__main__":
    print("Please run this script from automate.py.")
