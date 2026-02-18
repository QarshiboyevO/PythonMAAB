from bs4 import BeautifulSoup

# Load HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract table rows
rows = soup.find("tbody").find_all("tr")

weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))
    condition = cols[2].text
    weather_data.append((day, temp, condition))

# Display weather data
print("Weather Forecast:")
for day, temp, condition in weather_data:
    print(day, temp, "°C", condition)

# Highest temperature
max_temp = max(weather_data, key=lambda x: x[1])[1]
hottest_days = [d for d, t, c in weather_data if t == max_temp]

print("\nHighest Temperature:", max_temp, "°C")
print("Day(s):", hottest_days)

# Sunny days
sunny_days = [d for d, t, c in weather_data if c == "Sunny"]
print("\nSunny Day(s):", sunny_days)

# Average temperature
avg_temp = sum(t for d, t, c in weather_data) / len(weather_data)
print("\nAverage Temperature:", avg_temp, "°C")

import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

URL = "https://realpython.github.io/fake-jobs"
conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    PRIMARY KEY (title, company, location)
)
""")

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    link = job.find("a", text="Apply")["href"]

    # Check existing record
    cur.execute("""
        SELECT description, link FROM jobs
        WHERE title=? AND company=? AND location=?
    """, (title, company, location))

    result = cur.fetchone()

    if result is None:
        # Insert new job
        cur.execute("""
            INSERT INTO jobs VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, link))
    else:
        # Update if changed
        if result[0] != description or result[1] != link:
            cur.execute("""
                UPDATE jobs
                SET description=?, link=?
                WHERE title=? AND company=? AND location=?
            """, (description, link, title, company, location))

conn.commit()


# Filter & export to CSV
def export_jobs(filter_value, by="location"):
    cur.execute(f"""
        SELECT * FROM jobs WHERE {by}=?
    """, (filter_value,))

    rows = cur.fetchall()

    with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)


# Example usage
export_jobs("Remote")

conn.close()

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.demoblaze.com/"
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

laptops = []

# Find laptop cards
items = soup.find_all("div", class_="card-block")

for item in items:
    name = item.find("h4", class_="card-title").text.strip()
    price = item.find("h5").text.strip()
    description = item.find("p", class_="card-text").text.strip()

    laptops.append({
        "name": name,
        "price": price,
        "description": description
    })

# Save to JSON
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4)

print("Laptop data saved to laptops.json")