from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# Initialize the WebDriver with Service
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the web
driver.get("https://fbref.com/en/comps/9/stats/Premier-League-Stats")

# Get data
time.sleep(6)
table = driver.find_element(By.ID, 'stats_standard')
header_elements = table.find_elements(By.TAG_NAME, 'th')
headers = [header.text for header in header_elements]
rows = table.find_elements(By.TAG_NAME, 'tr')
data = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if cells:
        player_data = [cell.text if cell.text else 'N/a' for cell in cells]
        data.append(player_data)

# Sort data alphabetically
data.sort(key=lambda x: (x[0], int(x[4]) if x[4].isdigit() else 0))  # Age is at index 4

# Set headers
csv_headers = [
    'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born',
    'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 
    'G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 
    'xG', 'npxG', 'xAG', 'npxG+xAG', 
    'PrgC', 'PrgP', 'PrgR',
    'Gls', 'Ast', 'G+A', 'G-PK', 'G+A-PK', 
    'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG+xAG', 'Matches'
]

# Save data to a CSV file
with open('./Results/results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    writer.writerows(data)

driver.quit()

print("Successfully!")
