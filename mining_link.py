from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the file for writing
with open('extracted_links.txt', 'w') as file:
    # Loop through all the pages
    for page in range(1,5970 ):  # Assuming there are 5971 pages
        url = f"https://gptstore.ai/gpts?page={page}"
        driver.get(url)
        time.sleep(1)  # Wait for the page to load

        # Extract links from the current page
        elements = driver.find_elements(By.CLASS_NAME, "self-start")
        for element in elements:
            href = element.get_attribute('href')
            full_link = "https://gptstore.ai" + href
            file.write(full_link + '\n')  # Write each link to the file

        print(f"Completed page {page}")

driver.quit()

print("All links have been saved to 'extracted_links.txt'")
