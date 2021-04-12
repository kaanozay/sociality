import requests
import pymongo




def listingProducts():  #this function shows all products on database in prodcuts page. #Listing Products Function
   

    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    mydb = myclient["admin"]
    mycol = mydb["products"]
    

    return mycol.find()

