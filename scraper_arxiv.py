from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests 

subject = ["Physics", "Mathematics", "Computer_Science", "Biology", "Engineering", "Statistics", "Economics", "Finance"]

subfield_physics = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex", "nucl-th", "physics", "quant-ph"]

subfield_maths = ["math.AG", "math.AT", "math.AP", "math.CT", "math.CA", "math.CO", "math.AC", "math.CV", "math.DG", "math.DS", "math.FA", "math.GM", "math.GN", "math.GT", "math.GR", "math.HO", "math.IT", "math.KT", "math.LO", "math.MP", "math.MG", "math.NT", "math.MA", "math.OA", "math.OC", "math.PR", "math.QA", "math.RT", "math.RA", "math.SP", "math.ST", "math.SG"]

title_csv=[]
url_csv=[]
authors_csv=[]
category_csv=[]

def field(subject): 
	if subject == "Physics" :
		subsubject = subfield_physics
	elif subject == "Mathematics" :
		subsubject = subfield_maths
	else :
		subsubject = f"{subject}"	
	return subsubject
	
def arxiv(subject):
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
  		print(category.text.strip())
  		print(field(subject))
  		input()
  		if any(category.text.strip() == field(subject) for item in field(subject)) :
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
	 		
 


