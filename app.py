from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')

starTable = soup.find_all('table')


tempList= []
tableRows = starTable[4].find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)



Star_Names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(tempList)):
    
    Star_Names.append(tempList[i][0])
    Distance.append(tempList[i][5])
    Mass.append(tempList[i][7])
    Radius.append(tempList[i][8])

df = pd.DataFrame(list(zip(Star_Names,Distance,Mass,Radius,)),columns=['Star_Names','Distance','Mass','Radius'])
df.to_csv('final.csv')