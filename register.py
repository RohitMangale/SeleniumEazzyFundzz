from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import REGISTRATION_URL, REGISTRATION_DATA
from locators import RegistrationPageLocators
from utils import upload_file, select_dropdown_option

def test_registration(driver):
    driver.get(REGISTRATION_URL)

    # Fill out the registration form
    driver.find_element(*RegistrationPageLocators.FULL_NAME_FIELD).send_keys(REGISTRATION_DATA["full_name"])
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(REGISTRATION_DATA["email"])
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_DATA["password"])
    driver.find_element(*RegistrationPageLocators.PHONE_FIELD).send_keys(REGISTRATION_DATA["phone"])

    # Select user type and gender from dropdowns
    select_dropdown_option(driver, RegistrationPageLocators.USER_TYPE_DROPDOWN, REGISTRATION_DATA["user_type"])
    select_dropdown_option(driver, RegistrationPageLocators.GENDER_DROPDOWN, REGISTRATION_DATA["gender"])

    # Upload photo
    upload_file(driver, RegistrationPageLocators.UPLOAD_PHOTO_BUTTON, REGISTRATION_DATA["photo_path"])

    # Wait until the photo is uploaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "previewImg"))  # Adjust this to match actual selector
    )

    # Click the "Register" button
    driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    # Wait for registration completion
    sleep(5)

if __name__ == "__main__":
    print("Please run this script from automate.py.")
