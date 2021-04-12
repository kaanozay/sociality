import flask
from flask import Flask, render_template,request,redirect
from scraping import getDataEtsy
from product_data import productData
from listingFunc import listingProducts
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://host.docker.internal:27017/admin"
mongo = PyMongo(app)

data=()
images=[]
link=""
productid=""
@app.route("/")
def home():
    return render_template("test.html")

@app.route("/",methods=['POST'])
def getUrl():

    link=request.form['text_name']
    getDataEtsy(link)
    return render_template("test.html")


@app.route("/productPage.html")
def product():
    return render_template("productPage.html")
       
  
@app.route("/productsPage.html",methods=['POST','GET'])
def products():
    
    
    if request.method == 'POST':  
        productid=request.form['text']
         
        datas=productData(int(productid))
        
        price=datas['price']
        name=datas['name']
        image= datas['image'] 
        return render_template("productPage.html",name=name,price=price,image=image)
    else:
        liste: list =[]  
        values:list=listingProducts()
        
        for i in values:
        
            d={}
            d['_id']=str(i['_id'])
            d['image']=i['image']  
            d['name']=i['name']
            d['price']=i['price']

            
            liste.append(d)
            
        
        return render_template("productsPage.html",data=liste)
    
   



    
if __name__ == "__main__":
    app.run(debug=True)
