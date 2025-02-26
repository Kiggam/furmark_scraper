from bs4 import BeautifulSoup
import requests
import sqlite3
import re

conn = sqlite3.connect('/home/kiggam/Desktop/furmark_scraper/results.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS furmark(
    num INTEGER PRIMARY KEY,
    id INTEGER UNIQUE,
    gpu TEXT,
    score INTEGER,
    preset TEXT,
    time TEXT)
    ''')

response = requests.get('https://gpuscore.top/furmark/')
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all('tr')

id_pattern = r"id=([0-9]*?)\""
gpu_pattern = r"(.*?)(?:/|$)"

for i in range(1, len(table)):
    temp_lst = list(table[i])

    ids = re.search(id_pattern, str(temp_lst[2])).group(1)
    gpu = re.search(gpu_pattern, temp_lst[3].text).group(1)
    score = temp_lst[2].text
    preset = temp_lst[1].text
    time = temp_lst[4].text

    cursor.execute("""
    INSERT OR IGNORE INTO furmark (num, id, gpu, score, preset, time) 
    VALUES ((SELECT COALESCE(MAX(num), 0) + 1 FROM furmark), ?, ?, ?, ?, ?)
    """, (ids, gpu, score, preset, time))

conn.commit()
conn.close()
