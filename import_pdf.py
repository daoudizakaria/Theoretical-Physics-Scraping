from pathlib import Path
import os, sys, stat
import pandas as pd
import requests
import scraper_arxiv as scraper


scraper.arxiv()

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
 category.write_bytes(response.content)

