import requests
from bs4 import BeautifulSoup
import json
import time
from kafka import KafkaProducer

# Initialize variables
data = []
cnt = 0
url = "https://scrapeme.live/shop/"

while cnt == 0:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product links on the current page
    product_links = soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
    links = [link.get('href') for link in product_links]

    # Collect product data from each link
    for link in links:
        response2 = requests.get(link)
        soup2 = BeautifulSoup(response2.text, 'html.parser')

        # Extract description
        description_element = soup2.select_one('.woocommerce-product-details__short-description')
        description = description_element.text.strip() if description_element else "Description not found"

        # Extract stock number
        stock_element = soup2.select_one('.stock')
        stock = stock_element.text.strip() if stock_element else "Stock information not found"

        # Extract title
        title_element = soup2.find('h1', class_='product_title entry-title')
        title = title_element.text.strip() if title_element else "Title information not found"

        # Extract price
        price_element = soup2.select_one('.price')
        price = price_element.text.strip() if price_element else "Price information not found"

        # Append product data to list
        data.append({"title": title, "price": price, "description": description, "stock": stock})

    # Go to next page
    next_page_link = soup.find('a', class_='next page-numbers')
    if next_page_link:
        url = next_page_link.get('href')
    else:
        cnt = 1  # Exit loop if no next page

    #time.sleep(1)  # 1-second interval

# Print collected data
with open('/mnt/data/products.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Data saved to products.json")
