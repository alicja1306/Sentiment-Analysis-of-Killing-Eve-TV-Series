from selenium import webdriver      
from bs4 import BeautifulSoup
import pandas as pd
   
driver = webdriver.Chrome(executable_path = "/Users/alicja/Downloads/chromedriver")

url = ['https://www.rottentomatoes.com/tv/killing_eve/s01/reviews?type=user', 'https://www.rottentomatoes.com/tv/killing_eve/s02/reviews?type=user', 'https://www.rottentomatoes.com/tv/killing_eve/s03/reviews?type=user']
    
star = 0
sentiment = [] 
reviews = [] 

for page in url: 
    driver.get(page)
    while True:
        soup = BeautifulSoup(driver.page_source, 'lxml') 
        stars = soup.find_all('span', {'class':'star-display'})
      
        for i, item in enumerate(stars):
            if item.find_all('span', {'class':'star-display__filled'}):
                star = len(item.find_all('span', {'class':'star-display__filled'}))
            if item.find('span', {'class':'star-display__half'}):
                star = star + 0.5
            sentiment.append(star)
    
        review = soup.find_all('p', {'class':'audience-reviews__review--mobile js-review-text clamp clamp-4 js-clamp'})
        for i in review:
            reviews.append(i.text)
        
        try:
            nextbutton = driver.find_element_by_css_selector('#content > div > div > nav:nth-child(4) > button.js-prev-next-paging-next.btn.prev-next-paging__button.prev-next-paging__button-right > span')
            nextbutton.click()
            time.sleep(5)
         except Exception as e:
            print(e)
            break

df = pd.DataFrame({'reviews': reviews , 'sentiment': sentiment})

df.to_csv('rotten_tomatoes_audience_reviews.csv', index=False) 
