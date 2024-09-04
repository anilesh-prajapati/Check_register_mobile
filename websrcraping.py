from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import csv

# Amazon India registration page URL
registration_url = "https://www.amazon.in/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&prevRID=9D4HNKVN89WVRHZB9J9H&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

# proxy configuration
proxy_url = " "

# Function to initialize the WebDriver with proxy and options
def init_driver(proxy=None):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Set proxy if provided
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Function to check if a mobile number is registered on Amazon
def check_amazon_registration(mobile_number, proxy=None):
    driver = init_driver(proxy)
    registration_status = None
    
    try:
        # Open Amazon registration page
        driver.get(registration_url)
        time.sleep(random.uniform(2, 5))  # Random delay to mimic human behavior

        # Locate and fill in the registration form fields
        name_field = driver.find_element(By.ID, "ap_customer_name")
        name_field.send_keys("Test User")  # Use a dummy name

        phone_field = driver.find_element(By.ID, "ap_phone_number")
        phone_field.send_keys(mobile_number)
        time.sleep(random.uniform(1, 3))

        password_field = driver.find_element(By.ID, "ap_password")
        password_field.send_keys("TestPassword123!")  # Use a dummy password
        time.sleep(random.uniform(1, 3))

        # Click on 'Verify Mobile Number' button
        verify_button = driver.find_element(By.ID, "continue")
        verify_button.click()
        time.sleep(random.uniform(3, 6))

        # Check for the alert message indicating the number is already in use
        if "Mobile number already in use" in driver.page_source:
            registration_status = "ALREADY registered"
            print(driver.page_source)
        else:
            registration_status = "NOT registered"
    
    except Exception as e:
        print(f"An error occurred while checking number {mobile_number}: {e}")
    
    finally:
        # Close the browser
        driver.quit()
    
    return registration_status

# Function to read mobile numbers from a CSV file
def read_mobile_numbers_from_csv(file_path):
    mobile_numbers = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            mobile_numbers.append(row[0])  # Assumes one number per line
    return mobile_numbers

# Function to save results to a CSV file
def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mobile Number", "Registration Status"])
        for result in results:
            writer.writerow(result)

# Main function to check multiple mobile numbers
def check_multiple_numbers(file_path, output_file_path, proxy):
    mobile_numbers = read_mobile_numbers_from_csv(file_path)
    results = []

    for i, number in enumerate(mobile_numbers):
        # Perform registration check using the proxy
        status = check_amazon_registration(number, proxy)
        results.append((number, status))
        print(f"Checked {i+1}/{len(mobile_numbers)}: {number} - {status}")

        # Random delay to prevent rate limiting
        time.sleep(random.uniform(5, 10))

    # Save results to a CSV file
    save_results_to_csv(results, output_file_path)
    print("Completed checking all numbers.")

# Usage
input_file_path = "mobile_numbers.csv"  # Replace with your input CSV file path
output_file_path = "registration_results.csv"  # Replace with your desired output file path

check_multiple_numbers(input_file_path, output_file_path, proxy_url)
