from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()

#! Log Handelling
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
options.add_argument('--disable-logging')
options.add_argument('--disable-dev-tools')
options.add_argument('--silent')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)

#! Start
driver = webdriver.Chrome(options=options)
query = input("What do you want to search: ").strip().replace(" ", "+")
url = f"https://www.amazon.com/s?k={query}"

print("🚀 Opening Amazon...")
driver.get(url)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="a-section a-spacing-small a-spacing-top-small"]'))
)

#! Processing
print("🔍 Searching for products...")
products = driver.find_elements(By.CSS_SELECTOR, 'div[class*="a-section a-spacing-small a-spacing-top-small"]')

print(f"✅ Found {len(products)} products.\n")

all_data = []

for product in products:
    try:
        #! Link And Title containing Element
        title_and_link_elem = product.find_element(By.CSS_SELECTOR, 'a[class*="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')

        #! Title
        title = title_and_link_elem.find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'span').text

        #! Link
        link = title_and_link_elem.get_attribute('href')

        #! Rating & Sold Count Containing Element
        rating_and_sold_elem = product.find_element(By.CSS_SELECTOR, 'div[class*="a-row a-size-small"]')

        #! Price Tag
        price = str(int(product.find_element(By.CSS_SELECTOR, 'span[class*="a-price-whole"]').text) + 1) + '$'

        try:
            rating = rating_and_sold_elem.find_element(By.CSS_SELECTOR, 'a[class*="a-popover-trigger a-declarative"]').get_attribute('aria-label')
        except:
            rating = "Nan"

        #! Sold Count
        try:
            sold = rating_and_sold_elem.find_element(By.CSS_SELECTOR, 'span[class*="a-size-base s-underline-text"]').text
        except:
            sold = "Nan"

        #! Appending All Data
        all_data.append([title, sold, rating, price, link])
    except Exception as e:
        continue  # silently ignore missing data

# Save to CSV
with open('daraz.csv', 'w', newline='', encoding='utf-8', errors='ignore') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Sold', 'Rating', 'Price', 'Link'])
    writer.writerows(all_data)

print("✅ Data saved to daraz.csv")

driver.quit()
