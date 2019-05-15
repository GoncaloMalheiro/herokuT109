from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return('Gonçalo Malheiro')

if __name__=='__main__':
    app.run()
