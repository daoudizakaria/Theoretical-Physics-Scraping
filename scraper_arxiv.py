from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests 

title_csv=[]
url_csv=[]
authors_csv=[]
category_csv=[]

def arxiv():
 	driver = webdriver.Chrome()
 	URL_arxiv = "https://arxiv.org/search/?query=lecture+notes&searchtype=all&source=header"
 	driver.get(URL_arxiv)
 	page = requests.get(URL_arxiv)
 	content = driver.page_source
 	soup = BeautifulSoup(page.content, "html.parser")
 	results = soup.find(id="main-container")
 	papers = results.find_all("li", class_="arxiv-result")
 	for ppri in papers:
  		title = ppri.find("p", class_="title is-5 mathjax")
  		authors = ppri.find("p", class_="authors")
	        url = ppri.find("a", href_="")
	        category = ppri.find("span", class_="tag is-small is-link tooltip is-tooltip-top")
	        title_csv.append(title.text.strip())
  		url_csv.append(url.text.strip())
  		authors_csv.append(authors.text.strip())
  		category_csv.append(category.text.strip())
  		df = pd.DataFrame({'Title':title_csv,'Authors':authors_csv,'Category':category_csv,'Reference':url_csv}) 
  		df['Authors'] = df['Authors'].str.replace('Authors:', '')
  		df['Authors'] = df['Authors'].replace('\\n', '', regex=True)
  		df['Authors'] = df['Authors'].replace('           ', '', regex=True)
  		df['Reference'] = df['Reference'].str.replace('arXiv:', '')
  		df.to_csv('arxiv_data.csv', index=False, encoding='utf-8') 
 


