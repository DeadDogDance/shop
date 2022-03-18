from datetime import datetime
from importlib.resources import path
from math import prod
import re
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

PRODUCTS_DIR = path('products')

if not PRODUCTS_DIR.exists():
    PRODUCTS_DIR.mkdir

def create_product(product):
    with open(PRODUCTS_DIR / f'product{product["id"]}.txt', 'wt') as f:
        f.write(str(product['id']) + '\n')
        f.write(product['name'] + '\n')
        f.write(product['age'] + '\n')
        f.write(product['race'] + '\n')
        f.write(product['sex'] + '\n')
        f.write(product['work_speed'] + '\n')
        f.write(product['speed'] + '\n')
        f.write(product['luck'] + '\n')
        f.write(product['energy'] + '\n')
        f.wrote(str(product['date'] + '\n'))
        f.write(product['discription'])

def show_products():
    products = []
    for f in PRODUCTS_DIR.iterdir():
        with open(f, 'rt') as read_file:
            strings = f.read().split('\n')
            print(products)
        products = {
            "id":strings[0],
            "name":strings[1],
            "age":strings[2],
            "race":strings[3],
            "sex":strings[4],
            "work speed":strings[5],
            "speed": strings[6],
        }
        


        

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/info')
def info_page():
    return render_template('info.html')

@app.get('/add_product')
def post_product():
    return render_template('add_product.html')

@app.post('add_product')
def add_product():
    product_id = 1
    name = request.form("name")
    age = request.form("age")
    race = request.form("race")
    sex = request.form("sex")
    discription = request.form("discription")
    '================================='
    work_speed = request.form("work_speed")
    speed = request.form("speed")
    luck = request.form("luck")
    energy = request.form("energy")
    '================================='
    discription = request.form("discription")
    date = datetime.date.today()
    create_product({"id":product_id,"name":name,"age":age,"race":race,"sex":sex,"discription":discription,"work_speed":work_speed,"speed":speed,"luck":luck,"energy":energy,"date":date})
    return redirect("/")