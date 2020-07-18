from bs4 import BeautifulSoup 
import requests
import pandas as pd 
import re

reviews = [] 
sentiment = [] 

def getData(season, page):
    res = requests.get(f'https://www.rottentomatoes.com/tv/killing_eve/s0{season}/reviews?type=&sort=&page={page}')
    soup = BeautifulSoup(res.text, 'lxml')
    
    rev = soup.find_all('div', {'class':'critic__review-quote'})
    review = [i.text for i in rev]
    
    sentiments = soup.find_all('div', {'class':'review_icon'})
    find_sentiment = re.findall(r'rotten|fresh',  str(sentiments))
    
    reviews.extend(review)
    sentiment.extend(find_sentiment)

min_season = 1
max_season = 3
min_page_numer = 1
max_page_numer = 6
        
for season in range(min_season,max_season+1):
    for page in range(min_page_number, max_page_number):
        getData(season, page)

df = pd.DataFrame({'reviews': reviews,'sentiment': sentiment})

df['sentiment'].replace(['fresh', 'rotten'], ['positive', 'negative'], inplace=True)

df = df.replace(r'\n', '', regex=True)

df.to_csv('rotten_tomatoes_reviews.csv', index=False)
