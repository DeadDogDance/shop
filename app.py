from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/info')
def info_page():
    return render_template('info.html')

@app.get('/post_product')
def post_product():
    return render_template('post_product.html')