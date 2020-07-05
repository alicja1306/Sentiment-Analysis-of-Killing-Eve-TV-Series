from selenium import webdriver      
from bs4 import BeautifulSoup
import pandas as pd

    
driver = webdriver.Chrome(executable_path="/Users/alicja/Downloads/chromedriver")

url = ['https://www.rottentomatoes.com/tv/killing_eve/s01/reviews?type=user','https://www.rottentomatoes.com/tv/killing_eve/s02/reviews?type=user','https://www.rottentomatoes.com/tv/killing_eve/s03/reviews?type=user']

    
star = 0
sentiment = [] # for storing scores 
reviews=[] # for storing reviews


for page in url: 
    driver.get(page)
    while True:
        soup=BeautifulSoup(driver.page_source, 'lxml') 

        stars=soup.find_all('span',{'class':'star-display'})

        for i,j in enumerate(stars):
            if j.find_all('span',{'class':'star-display__filled'}):
                star = len(j.find_all('span',{'class':'star-display__filled'}))
            if j.find('span',{'class':'star-display__half'}):
                star = star + 0.5
            sentiment.append(star)
    
        review=soup.find_all('p',{'class':'audience-reviews__review--mobile js-review-text clamp clamp-4 js-clamp'})
        for i in review:
            reviews.append(i.text)
        
        try:
            
            NextButton = driver.find_element_by_css_selector('#content > div > div > nav:nth-child(4) > button.js-prev-next-paging-next.btn.prev-next-paging__button.prev-next-paging__button-right > span')
            NextButton.click()
            time.sleep(5)
        
        except Exception as e:
            print(e)
            break
print("Complete")
        

# checking if reviews and sentiment have the same length
print(len(reviews)) 
print(len(sentiment))


df = pd.DataFrame({'reviews': reviews ,'sentiment': sentiment})


df.to_csv('rotten_tomatoes_audience_reviews.csv',index=False) 


