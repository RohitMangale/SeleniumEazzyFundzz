
# Selenium Automation for Crowd-Funding Website

This repository, **SeleniumEazzyFundzz**, contains a Selenium-based automation project designed to interact with the **Crowd-Funding** website, which is hosted in the separate repository [**Crowd-Funding**](https://github.com/RohitMangale/Crowd-Funding). The automation script focuses on testing and automating the funding campaign process.

## Features

- **Automated Login:** Automates user authentication to log in to the website.
- **Campaign Selection:** Simplifies selecting and navigating to specific campaigns.
- **Fund Campaign:** Completes the funding process step by step, including setting the funding amount.
- **Configurable Locators:** Centralized locators for easier maintenance and flexibility.
- **Reusable Utilities:** Predefined functions for common tasks like WebDriver setup.
- **Debug-Friendly:** Includes delays to observe each step during execution.

---

## Prerequisites

1. **Crowd-Funding Website Repository**: Clone and set up the [Crowd-Funding](https://github.com/RohitMangale/Crowd-Funding) repository. Ensure the project is running locally.
2. **Python 3.7+**: Ensure Python is installed on your system.
3. **Google Chrome**: Install the latest version of Chrome.
4. **ChromeDriver**: Download the compatible version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).

---

## Installation

1. Clone the **SeleniumEazzyFundzz** repository:
   ```bash
   git clone https://github.com/RohitMangale/SeleniumEazzyFundzz.git
   cd SeleniumEazzyFundzz
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure project settings:
   - Update `config.py` with the **Crowd-Funding** website's URL and test credentials.

---

## Project Structure

```
SeleniumEazzyFundzz/
├── locators.py              # Web element locators
├── utils.py                 # Utility functions for WebDriver and helper methods
├── config.py                # Configuration file for constants
├── automate.py              # Main automation script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Usage

1. Ensure the **Crowd-Funding** website is running.
2. Open a terminal in the `SeleniumEazzyFundzz` directory.
3. Run the automation script:
   ```bash
   python automate.py
   ```
4. Observe the step-by-step process as the script:
   - Logs into the **Crowd-Funding** platform.
   - Selects a campaign.
   - Completes the funding process.

---

## Customization

1. **Update Locators:**  
   - Modify locators in `locators.py` to reflect any changes in the **Crowd-Funding** website structure.

2. **Adjust Delays:**  
   - Update `sleep` durations in `automate.py` for debugging or observation purposes.

3. **Test Different Campaigns:**  
   - Change campaign identifiers in `locators.py` to test other campaigns.

---

## Troubleshooting

### Common Issues

- **ChromeDriver Issues:**
  Ensure ChromeDriver is installed and matches your Chrome version.

- **Website Not Loading:**
  Verify the **Crowd-Funding** website is running and accessible.

- **Element Not Found:**
  Check the locators in `locators.py` to ensure they match the website structure.

---

## Contributing

Contributions are welcome! If you'd like to improve this project:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **Crowd-Funding Repository**: [Crowd-Funding](https://github.com/RohitMangale/Crowd-Funding) serves as the base platform for this project.
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

For support or feedback, feel free to reach out!
