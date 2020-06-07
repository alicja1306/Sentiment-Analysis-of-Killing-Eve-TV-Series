from selenium import webdriver      
from bs4 import BeautifulSoup
import pandas as pd
    
driver = webdriver.Chrome(executable_path="/Users/alicja/Downloads/chromedriver")
driver.get('https://www.imdb.com/title/tt7016936/reviews?ref_=tt_urv')


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
        sentiments.append(0)

      
reviews=[]
for j in div:
    if j.find('div',{'class':"text show-more__control"}):
        reviews.append(j.find('div',{'class':"text show-more__control"}).text)
    else:
        reviews.append(0)  

print(len(sentiments))
print(len(reviews))
print(len(div))
        
df = pd.DataFrame({'reviews': reviews,'sentiment': sentiments})

df.head()

df.to_csv('imbd_reviews.csv',index=False)
