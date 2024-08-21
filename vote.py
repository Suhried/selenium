
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Provide the full path to the chromedriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a ChromeService instance with the correct executable path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Initialize Chrome WebDriver with the ChromeService instance
driver = webdriver.Chrome(service=chrome_service)

# Open the specified URL in the Chrome browser
driver.get("https://forms.gle/pfqmtTtetefUGncA8")

def select_option_7_and_submit():
    try:
        # Wait for the radio button associated with "Option 7" to be present on the page
        option_7_radio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "i23"))
        )

        # Click on the radio button for "Option 7"
        option_7_radio.click()

        print("Clicked on Option 7")

        # Add a small delay to ensure the radio button selection is processed
        time.sleep(1)

        submit_button = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
        submit_button.click()
        print("Clicked on the Submit button")

    except TimeoutException as e:
        print(f"Timed out waiting for the element: {e}")

# Call the function to select "Option 7" and submit the form
select_option_7_and_submit()

# Add a delay to keep the browser open for a certain duration (adjust as needed)
time.sleep(1)

# Close the browser window
driver.quit()











