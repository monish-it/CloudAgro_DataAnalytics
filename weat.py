# from requests_html import HTMLSession
# # headers={"Accept-Language": "en-US,en;q=0.9,ar;q=0.8"}
# s= HTMLSession()
# query='Tambaram'
# url= f'https://www.google.com/search?q=weather+{query}'
# r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
# print(r.html.find('span#wob_tm', first=True).text)
# # print(r.html.find('title', first=True).text)




# importing library
import requests
from bs4 import BeautifulSoup

# enter city name
city = "Avadi"

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
# humidity = soup.find('span', attrs={"id": "wob_hm"}).text
# print(soup.find('span#wob_hm', first=True).text)

# str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
# humidity= soup.find('span', attrs={'id': 'wob_hm'}).text

# formatting data
# data = str.split('\n')
# time = data[0]
# sky = data[1]

# getting all div tag
# listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
# strd = listdiv[5].text

# getting other required data
# pos = strd.find('Wind')
# other_data = strd[pos:]

# printing all data
print(temp)
# print(humidity)

# print("Time: ", time)
# print("Sky Description: ", sky)
# print(other_data)
