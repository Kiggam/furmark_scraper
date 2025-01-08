from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('results.db')
cursor = conn.cursor()

conn.close()

# response = requests.get('https://gpuscore.top/furmark/')
# soup = BeautifulSoup(response.text, 'html.parser')
#
# lst = soup.find_all('tr')
#
# for i in range(1, len(lst)):
#     for l in list(lst[i]):
#         print(l)
