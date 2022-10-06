import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/corinthians', methods = ['POST'])
def serialize():
    nome = request.form['_first_name']
    time = request.form['_last_name']
    posicao = request.form['_posicao']
    return jsonify(_first_name = nome.upper(), _last_name = time.upper(), _posicao = posicao.upper())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5008))
    app.run(host = '0.0.0.0', port = port )
