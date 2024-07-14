from bs4 import BeautifulSoup
import requests
import helper_functions as hf

# Get html code form arch linux news page
source = requests.get("https://archlinux.org/").text

# Parse the html code
soup = BeautifulSoup(source, "lxml")

# Get news section from the html code
news_div = soup.find("div", id="news")
news_dict = {}

# From news section get all news and its respective link and add to dict
for news in news_div.find_all("h4"):
    news_dict[news.a.text] = "https://archlinux.org" + news.a["href"]

# Print the news
hf.print_news(news_dict, "\n")