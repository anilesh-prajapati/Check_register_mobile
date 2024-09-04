# Amazon Mobile Number Registration Checker

This project provides a Python script that automates the process of checking if a mobile number is already registered on Amazon India.

## Code Overview

### Proxy Configuration

The `proxy_url` is set to a server that handles IP rotation. This setup is crucial to avoid Amazon blocking your IP due to repeated requests from the same location.

### Initialize WebDriver with Proxy (`init_driver` function)

The `init_driver` function sets up the Chrome WebDriver with the provided proxy. The `chrome_options` allows you to configure the WebDriver, including setting the proxy.

### Check Registration Status (`check_amazon_registration` function)

The `check_amazon_registration` function automates the process of filling in the Amazon registration form with a name, mobile number, and password. It then checks for any message indicating whether the mobile number is already registered.

### Reading and Writing CSV Files

The `read_mobile_numbers_from_csv` function reads the input CSV file containing mobile numbers. The `save_results_to_csv` function saves the results to a CSV file.

### Main Logic for Checking Multiple Numbers (`check_multiple_numbers` function)

The `check_multiple_numbers` function loops through all the mobile numbers, checks each one, and saves the results. It uses a proxy for each check to rotate IP addresses and mimic natural browsing behavior.

## How to Use the Script

### 1. Prepare Your CSV Files

Make sure your `mobile_numbers.csv` file is formatted correctly with one mobile number per line.

### 2. Run the Script

Execute the script in your Python environment. Ensure your proxy server is set up correctly and working. The script will check each number and log the results to `registration_results.csv`.

### 3. Check the Results

After running the script, open `registration_results.csv` to see the status of each mobile number—whether it’s already registered or not.

## Additional Notes

- **Be Prepared for CAPTCHAs**: Amazon might display CAPTCHAs or other verification methods to block automated access. Consider how to handle this if it becomes an issue.
- **Stay Within Legal and Ethical Boundaries**: Ensure that you are using this script for legitimate purposes and comply with Amazon's terms of service and privacy policies.
- **Monitor Your Proxy Usage**: Keep an eye on how many requests you are making and ensure you are not exceeding any limits set by your proxy provider or facing additional charges.
