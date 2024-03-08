
# Get the URL https://webscraper.io/test-sites/e-commerce/allinone using requests library.
# You will see some selling items. Scrape the details of each item(e.g. name, price, number of reviews, ...) using BeautifulSoup. 
# Save the scraped data in a text file.
# Handle errors.
import requests
from bs4 import BeautifulSoup
import pandas as pd

def Send_Request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(e)


url = "https://webscraper.io/test-sites/e-commerce/allinone"
soup = BeautifulSoup(Send_Request(url), 'html.parser')


important_info = soup.find_all("div", class_ = 'card-body')

ls = []
for info in important_info:
    title = info.find("a", class_ = "title").text

    description = info.find('p', class_="description card-text").text

    price = info.find('h4', class_ = 'float-end price card-title pull-right').text

    num_of_review = info.find('p', class_='float-end review-count').text[0]
    
    rating_div = info.find('div', class_='ratings')
    p_in_div = rating_div.find_all("p")
    rating = len(p_in_div[1].find_all('span'))



    ls.append([title,description,price,num_of_review, rating])

data_frame = pd.DataFrame(ls, columns = ['Title','Description', "Price","Review_Count",'Rating'])
data_frame.to_csv('WebScraper.txt',index=False)

