import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP GET request to the target website
url = "https://www.example.com"  # Replace with the URL of the e-commerce website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Create a list to store the extracted product information
products = []

# Find the HTML elements containing the product information and iterate through them
product_elements = soup.find_all("div", class_="product")  # Replace with the appropriate HTML element and class for the product listings
for product_element in product_elements:
    # Extract the desired product details
    name = product_element.find("h2").text.strip()  # Replace with the appropriate HTML element for the product name
    price = product_element.find("span", class_="price").text.strip()  # Replace with the appropriate HTML element and class for the product price
    description = product_element.find("p").text.strip()  # Replace with the appropriate HTML element for the product description

    # Create a dictionary to store the product details
    product = {
        "Name": name,
        "Price": price,
        "Description": description
    }

    # Append the product dictionary to the list of products
    products.append(product)

# Save the extracted product information to a CSV file
filename = "product_information.csv"  # Replace with the desired filename
fields = ["Name", "Price", "Description"]  # Replace with the desired fields/columns for the CSV
with open(filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(products)

print("Scraping and CSV file creation complete!")