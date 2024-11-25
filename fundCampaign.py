from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils import initialize_webdriver
from locators import CampaignPageLocators

def fund_campaign(driver):
    try:
        # Step 1: Wait for the home page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "662e4822a3e682b703932e8a"))  # Replace with actual ID or element
        )

        # Step 2: Click on the campaign
        campaign_button = driver.find_element(*CampaignPageLocators.CAMPAIGN_BUTTON)
        # Scroll into view and wait for clickability
        driver.execute_script("arguments[0].scrollIntoView(true);", campaign_button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CampaignPageLocators.CAMPAIGN_BUTTON)).click()

        # Step 3: Wait for the campaign page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fundButton"))  # Replace with actual ID or element
        )

        # Step 4: Click on the "Fund" button
        fund_button = driver.find_element(*CampaignPageLocators.FUND_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", fund_button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CampaignPageLocators.FUND_BUTTON)).click()

        # Step 5: Wait for the funding page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fundAmountField"))  # Replace with actual ID or element
        )

        # Step 6: Enter the amount to fund
        fund_amount_field = driver.find_element(*CampaignPageLocators.FUND_AMOUNT_FIELD)
        fund_amount_field.send_keys("1000")

        # Step 7: Click the "Fund" button to complete the funding process
        confirm_button = driver.find_element(*CampaignPageLocators.FUND_CONFIRM_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CampaignPageLocators.FUND_CONFIRM_BUTTON)).click()

        # Wait a bit for the process to complete
        sleep(5)

    except Exception as e:
        print(f"An error occurred during the funding process: {e}")

if __name__ == "__main__":
    driver = initialize_webdriver(headless=False)
    fund_campaign(driver)
    driver.quit()
