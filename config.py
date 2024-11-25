# Configuration file

# Path to your WebDriver executable
WEBDRIVER_PATH = "./chromedriver-win64\chromedriver.exe"

# Website URL
LOGIN_URL = "http://localhost:5173/login"

LOGIN_DATA = {
    "email": "matt@gmail.com",
    "password": "matt",
}


CAMPAIGN_URL = "http://localhost:5173/"

REGISTRATION_URL = "http://localhost:5173/register"

REGISTRATION_DATA = {
    "full_name": "Matthew Langford Perry",
    "email": "matt@gmail.com",
    "password": "matt",
    "phone": "1234567890",
    "user_type": "Investor",  # Dropdown value
    "gender": "Male",  # Dropdown value
    "photo_path": r"D:\rohit\webDev\projects\Selenium\assets\perry.jpg",
}

