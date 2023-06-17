from pathlib import Path
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
 arxiv_url = f"https://arxiv.org/pdf/{matrix_data[i,3]}.pdf"
 print("The filename :", filename)
 print("the url :", arxiv_url)
 response = requests.get(arxiv_url)
 filename.write_bytes(response.content)

