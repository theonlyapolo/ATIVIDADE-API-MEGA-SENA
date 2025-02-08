import sqlite3 as sql

def criarTabela():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS apimegasena')

    comando = '''CREATE TABLE "apimegasena" (
        data TEXT,
        resultadoOrdemSorteio TEXT,
        resultadoListaDezena TEXT
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

def inserirInfo():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('insert into apimegasena (data, resultadoOrdemSorteio, resultadoListaDezena) values(?,?,?)', (data, resultadoOrdemSorteio_string, resultadoListaDezena_string))
    con.commit()
    con.close()

criarTabela()