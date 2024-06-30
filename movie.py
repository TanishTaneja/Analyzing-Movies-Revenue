from bs4 import BeautifulSoup
import requests
import pandas as pd

li=[]
page=101
while(page<=6001):
    url=f"https://www.the-numbers.com/movie/budgets/all/{page}"
    print(page)
    response=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

    soup=BeautifulSoup(response.content,'html.parser')

    table=soup.find('table')


    rows=table.find_all("tr")
    for a in rows[1:]:
        validate=a.text.split("\n")
        data={
            "Release_Date":validate[1],
            "Movie_Title":validate[2],
            "USD_Production_Budget":validate[3],
            "USD_Worldwide_Gross":validate[4],
            "USD_Domestic_Gross":validate[5]
        }
        li.append(data)
    page+=100

df=pd.DataFrame(li)
df.to_csv("cost_revenue.csv")
