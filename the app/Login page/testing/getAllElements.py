from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Set up the Selenium driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)

# Open the application
driver.get("http://localhost:5000/")

# Get all elements
all_elements = driver.find_elements(By.XPATH, "//*")

for element in all_elements:
    print(element.tag_name, element.get_attribute('id'), element.get_attribute('class'))

driver.quit()
