import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

# Define the number of test runs
num_runs = 1



# Additional runs for chat interaction
for i in range(num_runs):
    start_time = time.time()  # Record the start time

    # Set up the Selenium driver
    driver = webdriver.Chrome()

    # Open the application
    driver.get("http://localhost:5000/")

    # Test login functionality
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-panel.one'))).click()

    username_input = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'login-username')))
    password_input = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'login-password')))

    username_input.send_keys('test_user')
    password_input.send_keys('test_password')
    password_input.send_keys(Keys.RETURN)

    # Check if user is redirected to the homepage after login
    WebDriverWait(driver, 3).until(EC.url_to_be('http://localhost:5000/chatbot'))
    assert driver.current_url == 'http://localhost:5000/chatbot', "User not redirected to chat after login"

    # Test chat submission
    chat_input = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'chat-input')))
    chat_submit = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'chat-submit')))

    chat_input.send_keys('Hello, chat bot!')
    chat_submit.click()


    # Test sidebar toggle
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.sidebar-toggle'))).click()

    # Test sidebar links
    links = ['history', 'users', 'about', 'logout']
    for link in links:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.links a[href="/{link}"]'))).click()
        time.sleep(2)  # wait to see the effect
        
        # Go back to the dashboard
        if link != "logout":
            driver.back()
        
        time.sleep(1)  

    # Close the browser
    driver.quit()

    end_time = time.time()  # Record the end time
    duration = end_time - start_time  # Calculate the duration in seconds

    print("Test run was successful! " + f"Test {i + 1} took {duration:.2f} seconds")
