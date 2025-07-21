import requests
from bs4 import BeautifulSoup

site = requests.get(
    "https://www.climatempo.com.br/"
).content  # Fetching the content of the webpage

soup = BeautifulSoup(site, "html.parser")  # Using BeautifulSoup to parse HTML content

print(soup.title.string)  # Printing the prettified HTML content for better readability
# You can further process the soup object to extract specific data as needed.
print(soup.p.string)  # Printing the first paragraph content
