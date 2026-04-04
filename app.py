import json
import os
import random
from flask import Flask, render_template, abort

app = Flask(__name__)

# Lista oficial de curiosidades AdB / TUB
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
    # Escolha aleatória para o modo manutenção
    frase = random.choice(CURIOSIDADES_ADB)
    return render_template('manutencao.html', curiosidade=frase)

@app.route('/linha/<numero>')
@app.route('/linha/<numero>/<ano>')
@app.route('/linha/<numero>/<ano>/<sentido>')
def detalhe_linha(numero, ano="2026", sentido="ida"):
    # Lógica de carregamento do JSON da linha (que já tínhamos afinado)
    caminho = os.path.join('static', 'data', 'linhas', f'{numero}.json')
    if not os.path.exists(caminho):
        abort(404)
    with open(caminho, 'r', encoding='utf-8') as f:
        dados_totais = json.load(f)
    
    # ... processamento dos dados para o linha.html ...
    return render_template('linha.html', linha=dados_totais) # Simplificado para o exemplo

if __name__ == '__main__':
    # Porta 5002 para evitar bloqueios no Mac
    app.run(debug=True, port=5002)