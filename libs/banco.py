import sqlite3 as sql

def criarTabela():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS apimegasena')

    comando = '''CREATE TABLE "apimegasena" (
        data VARCHAR(150),
        dezena1 TEXT,
        dezena2 TEXT,
        dezena3 TEXT,
        dezena4 TEXT,
        dezena5 TEXT,
        dezena6 TEXT,
        dataProximoConcurso VARCHAR(150)
        )'''

    cur.execute(comando)
    con.close()

def verTabela():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute("select * from apimegasena")
    dados = cur.fetchall()
    con.close()
    return dados

def inserirInfo(data, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6, dataProximoConcurso):
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('insert into apimegasena (data, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6, dataProximoConcurso) values(?,?,?,?,?,?,?,?)', (data, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6, dataProximoConcurso))
    con.commit()
    con.close()

criarTabela()