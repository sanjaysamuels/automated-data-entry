from bs4 import BeautifulSoup
import lxml
import requests
from formFill import FillForm
import time

# Here you insert the webpage link to which you want to be scraped by making sure all the right filters are set
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

# Headers needed to access zillow webpage
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")

all_addresses = soup.select(".list-card-info address")
all_pricing = soup.select(".list-card-details li")
all_links = soup.select(".list-card-top a")

addresses = [listing.getText() for listing in all_addresses]
prices = [price.getText().split("+")[0] for price in all_pricing if "$" in price.text]
links = [listing.get("href") for listing in all_links]


# Bot that will automatically fill the scraped data into the form to create a spreadsheet
BOT = FillForm()
for i,j,z in zip(addresses,prices,links):
    time.sleep(2)
    BOT.new_form()
    BOT.fill_address(i)
    BOT.fill_price(j)
    BOT.fill_link(z)