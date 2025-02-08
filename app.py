from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def index():

    data = str(dados[0][0])
    resultadoOrdemSorteio = str(dados[0][1])
    resultadoListaDezena = str(dados[0][2])
    return render_template('index.html', resultadoOrdemSorteio=resultadoOrdemSorteio, data=data, resultadoListaDezena=resultadoListaDezena)

if __name__ == '__main__':
    app.run(debug=True)