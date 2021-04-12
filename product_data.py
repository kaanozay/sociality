import requests
import pymongo


def productData(id): #this function takes data from database by id for prodcut page. #Product Detail Function
    

    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    mydb = myclient["admin"]
    mycol = mydb["products"]

    for i in mycol.find():
        if i['_id']==id:
            return i


   

     