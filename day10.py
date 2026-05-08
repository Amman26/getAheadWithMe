1.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser
driver.maximize_window()

# Open Amazon homepage
driver.get("https://www.amazon.in")

# Wait for page to load
time.sleep(3)

# Capture page title
title = driver.title
print("Page Title:", title)

# Verify title contains Amazon
assert "Amazon" in title
print("Title verification passed")

# Click on Mobiles category
driver.find_element(By.LINK_TEXT, "Mobiles").click()

# Wait for mobiles page
time.sleep(3)

print("Navigated to Mobiles page")

# Navigate back to homepage
driver.back()

time.sleep(3)

print("Returned to Home Page")

# Close browser
driver.quit()
2.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for page to load
time.sleep(3)

# Locate search bar using ID
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter product name
search_box.send_keys("Wireless Headphones")

# Locate search button using XPath
search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")

# Click search button
search_button.click()

# Wait for search results page
time.sleep(3)

# Capture page source/text
page_text = driver.page_source

# Verify results are displayed
assert "Wireless Headphones" in page_text

print("Search results displayed successfully")

# Close browser
driver.quit()

3.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser window
driver.maximize_window()

# Implicit Wait
driver.implicitly_wait(10)

# Open Amazon website
driver.get("https://www.amazon.in")

# Locate search bar
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter laptop model
search_box.send_keys("Dell Inspiron 15")

# Click search button
driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
).click()

# Explicit Wait for first product image/result
wait = WebDriverWait(driver, 15)

first_product = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "(//img[contains(@class,'s-image')])[1]"
        )
    )
)

print("Search results loaded successfully")

# Click first product
first_product.click()

print("First product clicked successfully")

# Wait for product page
time.sleep(3)

# Close browser
driver.quit()

4.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser window
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for page to load
time.sleep(3)

# Scroll to footer section
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

# Click "About Us" using CSS Selector
about_us = driver.find_element(
    By.CSS_SELECTOR,
    "a[href*='aboutamazon']"
)

about_us.click()

# Wait for next page
time.sleep(3)

# Find an element using LINK_TEXT
career_link = driver.find_element(By.LINK_TEXT, "Careers")

# Print text content
print("Text Found:", career_link.text)

# Close browser
driver.quit()

5.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Open Amazon website
driver.get("https://www.amazon.in")

# Search for Smart Watches
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Smart Watches")

# Click search button
driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
).click()

# Explicit wait for search results
wait = WebDriverWait(driver, 15)

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@data-component-type='s-search-result']")
    )
)

print("Search results loaded")

# Click Samsung brand filter
samsung_brand = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//span[text()='Samsung']"
        )
    )
)

samsung_brand.click()

print("Samsung filter applied")

# Wait for page to refresh/update after filter
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Samsung')]")
    )
)

time.sleep(3)

# Count products displayed on first page
products = driver.find_elements(
    By.XPATH,
    "//div[@data-component-type='s-search-result']"
)

print("Number of products displayed:", len(products))

# Close browser
driver.quit()
