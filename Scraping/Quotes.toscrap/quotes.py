import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

url = "https://quotes.toscrape.com"
print("Accessing Page.....")
all_data = []

while True:
    html_page = requests.get(url).text
    soup = BeautifulSoup(html_page, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote_elem, author_elem in zip(quotes, authors):
        all_data.append([quote_elem.text.replace('“', '').replace('”', '').replace('"', '').strip(), author_elem.text])

    next_url = soup.find('li', class_='next')
    if next_url:
        url = urljoin(url, next_url.a["href"])
        print("Accessing Next Page....")
    else:
        break

# Save to CSV only once, after all scraping
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(all_data)

print("✅ Scraping complete. Data saved to quotes.csv")
