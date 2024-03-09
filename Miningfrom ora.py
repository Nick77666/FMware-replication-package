from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import csv

# Initialize the WebDriver
driver = webdriver.Chrome()

url = "https://ora.ai/explore"
driver.get(url)

data = []

try:
    while True:
        try:
            # Wait for the button to be clickable
            load_more_button = WebDriverWait(driver, 12).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.px-3.py-2.bg-primary-700'))
            )
            # Click the button
            driver.execute_script("arguments[0].click();", load_more_button)
            # Wait for a moment to let the page load more items
            WebDriverWait(driver, 5).until(EC.staleness_of(load_more_button))
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            # If the button is not clickable, not present, or obscured, break the loop
            break

    # Extract the data
    names = driver.find_elements(By.CSS_SELECTOR, 'div.max-w-\\[8\\.8rem\\].text-center.text-sm')
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'div.max-w-\\[8\\.8rem\\].text-xs.text-left')

    for name, description in zip(names, descriptions):
        data.append([name.text, description.text])

    # Append the extracted data to the CSV file
    with open('ora_ai_explore.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  # Move the cursor to the end of the file
        if file.tell() == 0:
            writer.writerow(['Name', 'Description'])
        writer.writerows(data)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
