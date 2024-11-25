# Locators for the login page
from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "email")  # Replace "email" with the actual ID
    PASSWORD_FIELD = (By.ID, "password")  # Replace "password" with the actual ID
    LOGIN_BUTTON = (By.ID, "loginButton")  # Replace "loginButton" with the actual ID

class RegistrationPageLocators:
    FULL_NAME_FIELD = (By.ID, "fullName")  # Replace "fullName" with the actual ID
    EMAIL_FIELD = (By.ID, "email")  # Replace "email" with the actual ID
    PASSWORD_FIELD = (By.ID, "password")  # Replace "password" with the actual ID
    PHONE_FIELD = (By.ID, "phone")  # Replace "phone" with the actual ID
    USER_TYPE_DROPDOWN = (By.ID, "userType")  # Replace "userType" with the actual ID
    GENDER_DROPDOWN = (By.ID, "gender")  # Replace "gender" with the actual ID
    UPLOAD_PHOTO_BUTTON = (By.ID, "customFile")  # Replace "uploadPhoto" with the actual ID
    SUBMIT_BUTTON = (By.ID, "signUpButton")  # Replace "signUpButton" with the actual ID



class CampaignPageLocators:
    # Add the locators specific to the campaign page
    CAMPAIGN_BUTTON = (By.ID, "662e4822a3e682b703932e8a")  # Replace with actual XPath or ID
    FUND_BUTTON = (By.ID, "fundButton")  # Replace with the actual ID of the fund button on the campaign page
    FUND_AMOUNT_FIELD = (By.ID, "fundAmountField")  # Replace with the actual ID of the input field for funding amount
    FUND_CONFIRM_BUTTON = (By.ID, "fundConfirmButton")  # Replace with the actual ID of the button that confirms the funding




