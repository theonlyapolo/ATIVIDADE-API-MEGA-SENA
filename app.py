from flask import Flask, render_template
import sqlite3 as sql
from libs.banco import verTabela

app = Flask(__name__)


@app.route('/')
def index():
    verTabela()
    data = dados[0]
    return render_template('index.html', dezena1=dezena1, dezena2=dezena2, dezena3=dezena3, dezena4=dezena4, dezena5=dezena5, dezena6=dezena6, data=data, dataProximoConcurso=dataProximoConcurso)

if __name__ == '__main__':
    app.run(debug=True)