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

PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 10> python  exercise1_navigation.py   

DevTools listening on ws://127.0.0.1:58438/devtools/browser/c647f4c6-8274-42ff-bf1e-940cde51225a
Page Title: Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
Title verification passed
[12148:12152:0508/204115.720:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
Navigated to Mobiles page
Returned to Home Page


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

PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 10> python  exercise2_search.py    

DevTools listening on ws://127.0.0.1:63890/devtools/browser/c945a88f-129e-4084-9695-a8d965fcf44d
[6200:8924:0508/205126.276:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
[6200:8924:0508/205126.698:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
[6200:8924:0508/205131.387:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
[6200:8924:0508/205131.816:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
Search results displayed successfully


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

PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 10> python  exercise3_waits.py 

DevTools listening on ws://127.0.0.1:59372/devtools/browser/86d04bca-9ff8-4ec3-ac88-1a4bd10ad8fc
[1204:6024:0508/205413.838:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
[1204:6024:0508/205414.535:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
Search results loaded successfully
First product clicked successfully

4.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "navFooter"))
)

# Scroll to footer section
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for footer to be visible
time.sleep(2)

# Click "About Us" safely
about_us = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='aboutamazon']"))
)
driver.execute_script("arguments[0].click();", about_us)  # JS click avoids interception

# Wait for next page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Careers"))
)

# Find an element using LINK_TEXT
career_link = driver.find_element(By.LINK_TEXT, "Careers")
print("Text Found:", career_link.text)

# Close browser
driver.quit()

                                                                                                        
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 10> python  exercise4_locators.py

DevTools listening on ws://127.0.0.1:56970/devtools/browser/d59419be-e1a4-4c7f-91ad-e83ea46429e5
[10316:10516:0508/210136.935:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
[10316:10516:0508/210138.831:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
Text Found: Careers


5.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Open Amazon website
driver.get("https://www.amazon.in")

# Search for Smart Watches
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Smart Watches")

# Click search button
driver.find_element(By.ID, "nav-search-submit-button").click()

# Explicit wait for search results
wait = WebDriverWait(driver, 15)
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
)
print("Search results loaded")

# Expand brand filter section if needed
try:
    see_more = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='See more']"))
    )
    see_more.click()
    time.sleep(2)
except:
    print("No 'See more' link found, continuing...")

# Click Samsung brand filter
samsung_brand = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung']"))
)
driver.execute_script("arguments[0].click();", samsung_brand)  # safer click
print("Samsung filter applied")

# Wait for page to refresh/update after filter
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Samsung')]"))
)

time.sleep(3)

# Count products displayed on first page
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
print("Number of products displayed:", len(products))

# Close browser
driver.quit()


PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 10> python  exercise5_filters.py

DevTools listening on ws://127.0.0.1:57561/devtools/browser/8ba96c6f-1caf-4fe7-9326-c4d17227febb
[1768:1408:0508/210703.561:ERROR:chrome\browser\task_manager\providers\fallback_task_provider.cc:126] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/40528867.
Search results loaded
Samsung filter applied
Number of products displayed: 16
