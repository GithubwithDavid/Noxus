import requests, csv

page = 1
all_quotes = []

while True:
    url = f"https://quotes.toscrape.com/api/quotes?page={page}"
    response = requests.get(url)
    data = response.json()

    for quote in data['quotes']:
        text = quote['text']
        author = quote['author']['name']
        all_quotes.append((text, author))

    if data['has_next'] == False:
        break

    page += 1

with open('quotes.csv', 'w', encoding='utf-8', newline='', errors='ignore') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    writer.writerows(all_quotes)
