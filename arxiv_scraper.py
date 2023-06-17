from pathlib import Path
import os, sys, stat
import pandas as pd
from tqdm.auto import tqdm
import requests
import scraper_arxiv as scraper

subject = ["Physics", "Mathematics", "Computer_Science", "Biology", "Engineering", "Statistics", "Economics", "Finance"]

subfield_physics = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex", "nucl-th", "physics", "quant-ph"]

subfield_maths = ["math.AG", "math.AT", "math.AP", "math.CT", "math.CA", "math.CO", "math.AC", "math.CV", "math.DG", "math.DS", "math.FA", "math.GM", "math.GN", "math.GT", "math.GR", "math.HO", "math.IT", "math.KT", "math.LO", "math.MP", "math.MG", "math.NT", "math.MA", "math.OA", "math.OC", "math.PR", "math.QA", "math.RT", "math.RA", "math.SP", "math.ST", "math.SG"]

i = 0
while i < len(subject):
	print(i,subject[i])
	i += 1 
 
choice = input("Choose the subject you want to scrape.\n")
choice_subject = str(choice)
x = 0
while x == 0 :
	URL_arxiv = f"https://arxiv.org/search/?searchtype=all&query=lecture+notes&abstracts=show&size=200&order=-announced_date_first&start={x}"
	scraper.arxiv(URL_arxiv,choice_subject)
	print(x)
	x += 200     	

df = pd.read_csv('arxiv_data.csv')
print("key",df)
matrix_data = df.to_numpy()
Len = len(matrix_data)
for i in range(Len) :
	filename = Path(matrix_data[i,0])
	category = Path(f"{matrix_data[i,2]}/{matrix_data[i,0]}.pdf")
	arxiv_url = f"https://arxiv.org/pdf/{matrix_data[i,3]}.pdf"
	print("--"*50)
	print("The filename :", filename)
	print("The category .", matrix_data[i,2])
	print("the url :", arxiv_url)
	response = requests.get(arxiv_url)
	total_size_in_bytes= int(response.headers.get('content-length', None))
	progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
	progress_bar.update(len(response.content))
	category.write_bytes(response.content)
