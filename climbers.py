# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:36:16 2020

@author: Gerard
"""


from bs4 import BeautifulSoup
import requests



headers = {
    'authority': 'peakbagger.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'ASP.NET_SessionId=aqgphzvmdi31w5pqeecf4w4b; __qca=P0-994950319-1585931807266',
}

params = (
    ('let', '1'),
)

def get_page_content():   
    response = requests.get('https://peakbagger.com/ClimbIndx.aspx', headers=headers, params=params)
    return response.content
    ### The comment below came from the converter ####
    
    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://peakbagger.com/ClimbIndx.aspx?let=1', headers=headers)
    
    
    # In case I wanted to test that the url has been fetched
    # print(response.content)
def create_soup(content): 
    return BeautifulSoup(content, features="html.parser")
    #print(soup.prettify())
    
def get_data(soup):
    print('Rank,Climber Name,Home Location,Ascents,Most Recent Ascent,Most Recent Peak,Elev-ft,Peak Location', end = '\n')
    
    
    cells = []
    print('There are ', len(cells), 'Cells')
    # All the website data I want has the data within a tag called span with 
    # an id named 'SearchResults'.
    # It seems like the list of top climbers and connected data are also hidden 
    # inside the search box so the data is doubled
    # That's why I am trying to start my scraping from this point
    # If I do a simple find_all td then I get everything twice
    # So I created this find all list then the tds extracted from within that list
    # using a loop
      
    for searchResult in soup.find_all('span', attrs = {'id' :'SearchResults'}):
        for row in searchResult.find_all('td'):
            cells.append(row.string)
            
    
    for cell in cells:
        cell = str(cell).strip()
        # Don't need this 'Ascent List' col of data as its a hyperlink but text
        # is always the same
        # I would have loved to extract the linked data associated with the 
        # Ascent List hyperlinkbut I already spent so long on this task due 
        # to my powershell/csv issues 
        
        # Deleting the Ascent Column as not needed here, it's simply repeated
        if cell == 'Ascent List':
            print('' + '\n', end = '')
        elif ',' in cell:
            cell = cell.replace(',', '')
            print(cell, end=',')
        else:
            print(cell, end=',')
    #print('There are ', len(cells), 'Cells')
def main():
    data = get_page_content()
    soup = create_soup(data)
    get_data(soup)   

if __name__ == '__main__':
    main()    
## Please note that as mentioned in my email, because I was using 
# Anaconda Powershell prompt to create my csv files 
# I lost literally 10-15 hours doubting my code and hitting my head off
# the wall, searching for reasons why on the internet, trying fixes etc.

# I just tried the command line now and it works like a dream
    
## However I would have liked all that time to spend looking at testing
## rather than scraping the data
  


