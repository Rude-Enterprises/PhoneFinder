import requests
from bs4 import BeautifulSoup as BS

url = "https://geo.craigslist.org/iso/us"

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"}

response = requests.get(url, headers=headers)

soup = BS(response.content, "html.parser")

ul_lists = soup.find_all("ul")
city_list = soup.find("ul", class_="height6")

print(city_list)

city_dict = {}

for city in city_list.find_all("a"):
    city_dict[city.text] = city["href"]

print(city_dict)