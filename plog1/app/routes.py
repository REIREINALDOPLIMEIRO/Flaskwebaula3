from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    nome = 'REINALDO'
    Pssoa = {'Pessoa': 'Bruno Reinaldo', 'Idade': '22 anos '}
    return render_template('index.html', nome = nome, Pssoa = Pssoa)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)