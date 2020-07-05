from selenium import webdriver      
from bs4 import BeautifulSoup
import pandas as pd
    
driver = webdriver.Chrome(executable_path="/Users/alicja/Downloads/chromedriver")
driver.get('https://www.imdb.com/title/tt7016936/reviews?ref_=tt_urv')

# Load all the page data, by clicking Load More button.
while True:
    try:
        loadMoreButton = driver.find_element_by_class_name('load-more-data')
        loadMoreButton.click()
    except Exception as e:
        print(e)
        break
print("Complete")



soup=BeautifulSoup(driver.page_source, 'lxml') 

div=soup.find_all('div',{'class':'lister-item'})

sentiments=[]
for i in div:
    if i.find('span',{'class':'rating-other-user-rating'}):
        sentiments.append(i.find('span',{'class':'rating-other-user-rating'}).span.text)
    else:
        sentiments.append(0) #if user rate doesn't exist

      
reviews=[]
for i in div:
    if i.find('div',{'class':"text show-more__control"}):
        reviews.append(i.find('div',{'class':"text show-more__control"}).text)
    else:
        reviews.append(0) #if review doesn't exist
        

# checking if reviews and sentiments have the same length
print(len(sentiments))
print(len(reviews))


        
df = pd.DataFrame({'reviews': reviews,'sentiment': sentiments})

df.head()

data = df[df.sentiment != 0] #removing rows without user rate

data.to_csv('imbd_reviews.csv',index=False)


