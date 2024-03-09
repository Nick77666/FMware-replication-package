from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Initialize the WebDriver
driver = webdriver.Chrome()

data = []

# Iterate over the pages from p=0 to p=9
for i in range(10):
    url = f"https://huggingface.co/chat/assistants?p={i}"
    driver.get(url)

    # Extract the names and descriptions using the specified classes
    names = driver.find_elements(By.CLASS_NAME, 'line-clamp-2')
    descriptions = driver.find_elements(By.CLASS_NAME, 'line-clamp-4')

    # Store the extracted information in the data list
    for name, description in zip(names, descriptions):
        data.append([name.text, description.text])

# Write the extracted data to a CSV file
with open('HFassistants.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Description'])
    writer.writerows(data)

driver.quit()
