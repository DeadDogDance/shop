import datetime
from pathlib import Path
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

PRODUCTS_DIR = Path('products')

if not PRODUCTS_DIR.exists():
    PRODUCTS_DIR.mkdir()


def create_product(product):
    with open(PRODUCTS_DIR / f'product{product["id"]}.txt', 'wt') as f:
        f.write(str(product['id']) + '\n')  #0
        f.write(product['price'] + '\n')    #1
        f.write(product['name'] + '\n')     #2
        f.write(product['age'] + '\n')      #3
        f.write(product['race'] + '\n')     #4
        f.write(product['sex'] + '\n')      #5
        f.write(product['work_speed'] + '\n')#6
        f.write(product['speed'] + '\n')    #7
        f.write(product['luck'] + '\n')     #8
        f.write(product['energy'] + '\n')   #9
        f.write(str(product['date']) + '\n')#10
        f.write(product['description'])     #11 надо пофиксить переносы
                                            # дже-е-е-ейсо-о-он

def show_products():
    products = []
    for f in PRODUCTS_DIR.iterdir():
        with open(f, 'rt') as read_file:
            strings = read_file.read().split('\n')
        product = {
            "id":strings[0],
            "price":strings[1],
            "name":strings[2],
            "description":strings[11]
        }
        products.append(product)
    return products
        


        

@app.get('/')
def index():
    products = show_products()
    return render_template('index.html', products = products)

@app.get('/product_page/<id>')
def product_page(id):
    with open(PRODUCTS_DIR / f'product{id}.txt', 'rt') as f:
        strings = f.read().split('\n')
        product = {
            "id":strings[0],
            "price":strings[1],
            "name":strings[2],
            "age":strings[3],
            "race":strings[4],
            "sex":strings[5],
            "work_speed":strings[6],
            "speed":strings[7],
            "luck":strings[8],
            "energy":strings[9],
            "date":strings[10],
            "description":strings[11]
        }
    return render_template("product_page.html", product = product)
        


@app.get('/info')
def info_page():
    return render_template('info.html')

@app.get('/add_product')
def post_product():
    return render_template('add_product.html')

@app.post('/add_product')
def add_product():
    product_id = len(show_products())+1
    name = request.form["name"]
    age = request.form["age"]
    race = request.form["race"]
    sex = request.form["sex"]
    description = request.form["description"]
    # '================================='
    work_speed = request.form["work_speed"]
    speed = request.form["speed"]
    luck = request.form["luck"]
    energy = request.form["energy"]
    # '================================='
    price = request.form["price"]
    date = datetime.date.today()

    create_product({"id":product_id,"name":name,"age":age,"race":race,
                    "sex":sex,"description":description,"work_speed":work_speed,
                    "speed":speed,"luck":luck,"energy":energy,"price":price,"date":date})
    return redirect("/")