from flask import Flask, render_template
import sqlite3 as sql
from libs.banco import verTabela
from libs.api import main


app = Flask(__name__)


@app.route('/')
def index():
    main()
    dados = verTabela()
    data = dados[0][0]
    dezena1 = dados[0][1]
    dezena2 = dados[0][2]
    dezena3 = dados[0][3]
    dezena4 = dados[0][4]
    dezena5 = dados[0][5]
    dezena6 = dados[0][6]
    dataProximoConcurso = dados[0][7]
    return render_template('index.html', dezena1=dezena1, dezena2=dezena2, dezena3=dezena3, dezena4=dezena4, dezena5=dezena5, dezena6=dezena6, data=data, dataProximoConcurso=dataProximoConcurso)

if __name__ == '__main__':
    app.run(debug=True)