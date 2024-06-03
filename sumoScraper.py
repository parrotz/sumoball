import requests
from bs4 import BeautifulSoup
import pandas as pd

def sumoScraper():
    jan24 = 'https://sumodb.sumogames.de/Banzuke.aspx?b=202401&heya=-1&shusshin=-1&h=on&bd=on&hd=on&su=on&w=on&hr=on&ho=on&ch=on&cs=on&cr=on&spr=on&sps=on&snr=on&sns=on&c=on&simple=on'
    page = requests.get(jan24)

    soup = BeautifulSoup(page.content, 'html.parser')

    jan24Table = soup.find(class_='banzuke')

    colCount = len(jan24Table.find_all('th'))

    # Get column headers
    header = []

    for i in range(1, colCount):
        heads = jan24Table.findAll('th')
        header.append(heads[i - 1].text)

    header.append('Basho')
    sumo = pd.DataFrame(columns=header)


    # Get data for 1958-2024
    for year in range(1958,2024):
        for month in ['01', '03', '05', '07', '09', '11']:
            URL = 'https://sumodb.sumogames.de/Banzuke.aspx?b=' + str(year) + month + '&heya=-1&shusshin=-1&h=on&bd=on&hd=on&su=on&w=on&hr=on&ho=on&ch=on&cs=on&cr=on&spr=on&sps=on&snr=on&sns=on&c=on&simple=on'
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, 'html.parser')

            basho = soup.find(class_='layoutright').h1.text

            banzuke = soup.find(class_='banzuke')



print(sumo)