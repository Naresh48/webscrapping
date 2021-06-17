

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#connect webdriver to the chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

#to get the URL
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}): 
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'col col-5-12 _2o7WAb'})
    rating=a.find('div', attrs={'class':'niH0FQ'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 

#to save the dataframe into the csv file
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
