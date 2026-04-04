import json
import os
import random
from flask import Flask, render_template, abort

app = Flask(__name__)

CURIOSIDADES_ADB = [
    "A linha 99 foi inaugurada a 22 de setembro de 2025.",
    "Os primeiros autocarros elétricos de Braga começaram a circular em 2018.",
    "A AdB transporta mais de 12 milhões de passageiros por ano.",
    "A linha 02 é uma das mais antigas e emblemáticas da cidade.",
    "Em 2026, a AdB reforçou a ligação às zonas industriais com novos horários.",
    "O sistema de bilhética permite agora o pagamento direto com telemóvel.",
    "A frota da AdB percorre diariamente uma distância equivalente a meia volta ao mundo."
]

@app.route('/')
def manutencao():
    frase = random.choice(CURIOSIDADES_ADB)
    return render_template('manutencao.html', curiosidade=frase)

# Rota das linhas mantem-se como configurado anteriormente
@app.route('/linha/<numero>')
def detalhe_linha(numero):
    # ... lógica de carregamento do JSON ...
    return render_template('linha.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)