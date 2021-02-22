# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, request
from brands import Brand

app = Flask(__name__)

gucci = Brand(name='gucci')
supreme = Brand(name='supreme')
chanel = Brand(name='chanel')

brands = [gucci,supreme,chanel]

@app.route('/brands', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # gather the value of an input with a name attribute of "name"
        brands.append(Brand(request.form['name']))
        # respond with a redirect to the route which has a function called "index" (in this case that is '/toys')
        return redirect(url_for('index'))
    # if the method is GET, just return index.html
    return render_template('index.html', brands=brands)

@app.route('/brands/new')
def new():
    return render_template('new.html')

app.run(host="localhost", port=int("5000"))
