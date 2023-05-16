import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium driver
driver = webdriver.Chrome()

# Currently having issues with locating the correct element via CSS selector

# Open the application
driver.get('http://localhost:5000/index')

# Test registration functionality
register_links = driver.find_elements(By.CSS_SELECTOR, 'a[href="/register"]')
if len(register_links) > 0:
    register_links[0].click()

    username_input = driver.find_element(By.ID, 'register-username')
    password_input = driver.find_element(By.ID, 'register-password')
    confirm_password_input = driver.find_element(By.ID, 'confirm_password')
    email_input = driver.find_element(By.ID, 'email')

    username_input.send_keys('test_user')
    password_input.send_keys('test_password')
    confirm_password_input.send_keys('test_password')
    email_input.send_keys('test@example.com')

    driver.find_element(By.CSS_SELECTOR, '#register-form button[type="submit"]').click()

    # Wait for the registration response
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'register-response')))

    # Verify the registration response
    register_response = driver.find_element(By.ID, 'register-response')
    assert register_response.text == 'User registered.'
else:
    print("Register link not found.")

# Test login functionality
login_links = driver.find_elements(By.CSS_SELECTOR, 'a[href="/login"]')
if len(login_links) > 0:
    login_links[0].click()

    username_input = driver.find_element(By.ID, 'login-username')
    password_input = driver.find_element(By.ID, 'login-password')

    username_input.send_keys('test_user')
    password_input.send_keys('test_password')
    password_input.send_keys(Keys.RETURN)

    # Wait for the login response
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-response')))

    # Verify the login response
    login_response = driver.find_element(By.ID, 'login-response')
    assert login_response.text == 'Login successful.'
else:
    print("Login link not found.")

# Close the browser
driver.quit()
