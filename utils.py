from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def initialize_webdriver(headless=False):
    """Initialize the WebDriver with optional headless mode."""
    options = Options()
    if headless:
        options.add_argument("--headless")

    # Create the Service object with the path to chromedriver
    service = Service(executable_path="./chromedriver-win64/chromedriver.exe")  # Update this path

    # Use the Service object to initialize the driver
    return webdriver.Chrome(service=service, options=options)

def upload_file(driver, locator, file_path):
    """Upload a file."""
    driver.find_element(*locator).send_keys(file_path)

def select_dropdown_option(driver, locator, value):
    """Select an option from a dropdown."""
    from selenium.webdriver.support.ui import Select
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_visible_text(value)
