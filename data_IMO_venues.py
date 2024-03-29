import pandas as pd
import requests
from bs4 import BeautifulSoup

def table_scrapper(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "lxml")
    table = soup.find('table')

    #First I will extract the headers of the table with IMO venues
    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)

    if URL == "https://www.imo-official.org/organizers.aspx":
        headers.pop(-4)
        headers[2] = 'Host'
        print(headers)
    if URL == "https://www.imo-official.org/results.aspx":
        half = int((len(headers)/2))
        headers = headers[0:half] 

    mydata = pd.DataFrame(columns = headers)
    for j in table.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row
    
    return mydata

venues = table_scrapper("https://www.imo-official.org/organizers.aspx")
venues = venues[['Year', 'Host', 'Countries']]
venues = venues.iloc[3:]
venues = venues.set_index(['Year'])
venues['Countries'] = venues['Countries'].apply(pd.to_numeric)
venues.index.name = None
