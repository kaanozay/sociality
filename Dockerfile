FROM python:3.7

WORKDIR /app

RUN pip install flask
RUN pip install flask-mysqldb
RUN pip install beautifulsoup4
RUN pip install requests 
RUN pip install pip install pymongo
RUN pip install Flask-PyMongo


COPY . /app


ENV FLASK_APP=app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]