import requests
from bs4 import BeautifulSoup
import pymongo



def getDataEtsy(url): #this function gets datas from website and saves to database. #Adding Product Function
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    name = soup.find('h1',{'class': 'wt-text-body-03'} ).text.strip().replace('\n','')
    price = soup.find('p', {'class': 'wt-mr-xs-2'}).text.replace('+', '').strip().replace('£', '')
    image = soup.find('img',{'class': 'wt-max-width-full'})
    img=image.get('src')
    
    lastId=0
    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    mydb = myclient["admin"]
    mycol = mydb["products"]
    for i in mycol.find():
        lastId=lastId+1
    mydict = { "_id": lastId+1, "name": name, "image": img, "price": price }
    return mycol.insert_one(mydict)


