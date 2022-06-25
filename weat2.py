import requests
from bs4 import BeautifulSoup

city="Tambaram"
soup= BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+{city}").text, "html.parser")
print(soup.prettify())