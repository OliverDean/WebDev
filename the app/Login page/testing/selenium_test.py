import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

# Define the number of test runs
num_runs = 3


# Start the loop to run the test multiple times
for i in range(num_runs):
    start_time = time.time()  # Record the start time

    # Set up the Selenium driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3)


    # Open the application
    driver.get("http://localhost:5000/")
    random_string = ''.join(random.choices(string.digits, k=10))

    # Wait until the page is fully loaded
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    # Test registration functionality, this line took longer than all the rest of the code combined
    register_form = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-panel.two:not(.active)')))

    if register_form:
        register_form.click()
        username_input = driver.find_element(By.ID, 'register-username')
        password_input = driver.find_element(By.ID, 'register-password')
        confirm_password_input = driver.find_element(By.ID, 'confirm_password')
        email_input = driver.find_element(By.ID, 'email')

        username_input.send_keys('test_user' + random_string)
        password_input.send_keys('test_password' + random_string)
        confirm_password_input.send_keys('test_password' + random_string)
        email_input.send_keys('test' + random_string + '@example.com')

        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]#register-button')))

        driver.execute_script("arguments[0].click();", register_button)
        register_button.click()
        # Wait for the alert to be present
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    else:
        print("Register link not found.")

    # Test login functionality
    login_form = driver.find_element(By.CSS_SELECTOR, '.form-panel.one')
    if login_form:
        login_form.click()

        username_input = driver.find_element(By.ID, 'login-username')
        password_input = driver.find_element(By.ID, 'login-password')

        username_input.send_keys('test_user' + random_string)
        password_input.send_keys('test_password' + random_string)
        password_input.send_keys(Keys.RETURN)

        # Check if user is redirected to the homepage after login
        WebDriverWait(driver, 3).until(EC.url_to_be('http://localhost:5000/chatbot'))
        assert driver.current_url == 'http://localhost:5000/chatbot' , "User not redirected to chat after login"
        # Close the browser
        driver.quit()


    end_time = time.time()  # Record the end time
    duration = end_time - start_time  # Calculate the duration in seconds

    print("Test run was successful! " + f"Test {i + 1} took {duration:.2f} seconds")