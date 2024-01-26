from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the file for writing
with open('extracted_links.txt', 'w',encoding='utf-8') as file:
    # Loop through all the pages
    for page in range(1, 5970):  # Adjust the range as needed
        url = f"https://gptstore.ai/gpts?page={page}"
        driver.get(url)
        time.sleep(1)  # Wait for the page to load

        # Extract names and descriptions
        names = driver.find_elements(By.CLASS_NAME, "self-start")
        descriptions = driver.find_elements(By.CLASS_NAME, "h-12")

        # Ensure both lists have the same length
        if len(names) == len(descriptions):
            for name, description in zip(names, descriptions):
                # Only write if both name and description have text
                if name.text and description.text:
                    file.write(f"{name.text}, \" {description.text}\" \n")
        else:
            print(f"Warning: Mismatch in counts of names and descriptions on page {page}")

driver.quit()

print("All data have been saved to 'extracted_links.txt'")
