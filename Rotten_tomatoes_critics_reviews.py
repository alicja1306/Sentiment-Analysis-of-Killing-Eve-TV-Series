from bs4 import BeautifulSoup 
import requests
import pandas as pd 
import re

reviews=[] #for storing reviews
sentiment=[] #for storing the sentiment of reviews
date = [] #for storing dates

def getData(season,page):
    res = requests.get(f'https://www.rottentomatoes.com/tv/killing_eve/s0{season}/reviews?type=&sort=&page={page}')
    soup = BeautifulSoup(res.text,'lxml')
    
    rev=soup.find_all('div',{'class':'critic__review-quote'})
    review = [i.text for i in rev]
    
    sentiments=soup.find_all('div',{'class':'review_icon'})
    find_sentiment= re.findall(r'rotten|fresh',str(sentiments))
    
    dates = soup.find_all('div',{'class':'critic__review-date subtle small'})
    d = [i.text for i in dates]
    
    reviews.extend(review)
    sentiment.extend(find_sentiment)
    date.extend(d)
    
    
for season in range(1,4):
    for page in range(1,6):
        getData(season,page)

        
df = pd.DataFrame({'reviews': reviews,'sentiment': sentiment,'date':date})

df['sentiment'].replace(['fresh', 'rotten'], ['positive', 'negative'], inplace=True)

df = df.replace(r'\n',  '', regex=True)

df.to_csv('rotten_tomatoes_reviews.csv',index=False)