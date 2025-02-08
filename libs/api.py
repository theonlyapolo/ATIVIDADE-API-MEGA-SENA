import requests
import json
import sqlite3 as sql
from libs.banco import inserirInfo

def main():
    api_url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena'

    request = requests.get(api_url)

    if request.status_code == 200:
        dado = json.loads(request.text)

        data = dado["dataApuracao"]
        resultadoOrdemSorteio = dado["dezenasSorteadasOrdemSorteio"]
        dataProximoConcurso = dado["dataProximoConcurso"]

        dezena1, dezena2, dezena3, dezena4, dezena5, dezena6 = resultadoOrdemSorteio
        inserirInfo()

    else:
        print('Falha...')