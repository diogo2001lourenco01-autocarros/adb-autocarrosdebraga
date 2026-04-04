import json
import os
import random
from flask import Flask, render_template, abort

app = Flask(__name__)

# LISTA OFICIAL AdB
CURIOSIDADES_ADB = [
    "A linha 99 foi inaugurada a 22 de setembro de 2025.",
    "Os primeiros autocarros elétricos chegaram em 2018.",
    "A linha 97 foi inaugurada a 15 de setembro de 2025.",
    "A linha 98 foi inaugurada a 4 de novembro de 2024.",
    "Em 2026, os AdB vão lançar novas funcionalidades para todos os curiosos e entusiastas!"
]

@app.route('/')
def manutencao():
    # Sorteio aleatório
    frase = random.choice(CURIOSIDADES_ADB)
    return render_template('manutencao.html', curiosidade=frase)

@app.route('/linha/<numero>')
@app.route('/linha/<numero>/<ano>')
@app.route('/linha/<numero>/<ano>/<sentido>')
def detalhe_linha(numero, ano="2026", sentido="ida"):
    caminho_json = os.path.join('static', 'data', 'linhas', f'{numero}.json')
    if not os.path.exists(caminho_json):
        abort(404)
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return render_template('linha.html', linha=dados, ano=ano, sentido=sentido)

if __name__ == '__main__':
    # Porta 5001 conforme o teu terminal do Mac
    app.run(debug=True, port=5001)