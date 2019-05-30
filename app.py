from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/sobremesas')
def sobremesas():
    return render_template('sobremesas.html')

@app.route('/carne')
def carne():
    return render_template('carne.html')

@app.route('/mar')
def mar():
    return render_template('mar.html')

@app.route('/queijo')
def queijo():
    return render_template('queijo.html')


if __name__=='__main__':
    app.run(debug=True)
