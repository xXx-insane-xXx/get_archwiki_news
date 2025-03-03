# Archwiki Home Page News Scrapper :)

## Description
This python code gets you the latest news along with its links from arch wiki home page

## Usage
```
$ git clone --depth=1 https://github.com/xXx-insane-xXx/get_archwiki_news.git
$ pip install -r requirements.txt
$ python main.py
```

## Sample output
```
$ python main.py
1. The sshd service needs to be restarted after upgrading to openssh-9.8p1: https://archlinux.org/news/the-sshd-service-needs-to-be-restarted-after-upgrading-to-openssh-98p1/
2. Arch Linux 2024 Leader Election Results: https://archlinux.org/news/arch-linux-2024-leader-election-results/
3. Increasing the default vm.max_map_count value: https://archlinux.org/news/increasing-the-default-vmmax_map_count-value/
4. The xz package has been backdoored: https://archlinux.org/news/the-xz-package-has-been-backdoored/
5. mkinitcpio hook migration and early microcode: https://archlinux.org/news/mkinitcpio-hook-migration-and-early-microcode/

```

## Notes
~This repo is also for me to remind myself how to use bs4~ <br>
<hr>

```
from bs4 import BeautifulSoup
import requests
import helper_functions as hf
```
Imports necessary modules. <br>
<hr>

```
# Get html code form arch linux news page
source = requests.get("https://archlinux.org/").text

# Parse the html code
soup = BeautifulSoup(source, "lxml")
```
Get html source code and make a bs4 object which uses lxml to parse the content. <br>
<hr>

```
# Get news section from the html code
news_div = soup.find("div", id="news")
news_dict = {}
```
Returns a tag object. <br>
bs4_object.tag1.tag2 or bs4.object.find("tag") both returns tag object. <br>
bs4.find_all("tag") returns a tag_object which is wrapped as a list. <br>
<hr>

```
# From news section get all news and its respective link and add to dict
for news in news_div.find_all("h4"):
    news_dict[news.a.text] = "https://archlinux.org" + news.a["href"]
```
Iterate over the tag list object. <br>
<hr>

```
# Print the news
hf.print_news(news_dict, "\n")
```
Yea everyone knows what it would do. <br>
<hr>

