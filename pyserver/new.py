# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)
d1={2:"Cow",1:"Dog",3:"Cat"}
@app.route("/search/<animal>/",)
 
def search(animal):
 
    result = d1.get(int(animal),"Not Found")
    return result
 
@app.route("/insert/<animalnum>/<animal>/",)
 
def insert(animalnum,animal):
 
 
     d1[int(animalnum)]=animal
     return render_template('index.html', d1=d1)
 
@app.route("/")
 
def index():
     return render_template('index.html', d1=d1)
 
@app.route("/update/<animalnum>/<animal>/",)
 
def update(animalnum,animal):
 
 
     d1[int(animalnum)]=animal
     return render_template('index.html', d1=d1)
 
@app.route("/delete/<animalnum>/",)
 
def delete(animalnum):
 
    try:
        del( d1[int(animalnum)])
        return render_template('index.html', d1=d1)
    except:
        return "Not Found"
if __name__ == "__main__":
    #print(__name__)
    app.run(host="localhost", port=int("5000"))
    