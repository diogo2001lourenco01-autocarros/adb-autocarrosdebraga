import json
import os
import random # Importante para o sorteio
from flask import Flask, render_template, abort

app = Flask(__name__)

# Lista de curiosidades AdB / TUB
CURIOSIDADES_ADB = [
    "A linha 99 foi inaugurada a 22 de setembro de 2025, com o percurso Avenida Central — Santa Lucrécia.",
    "Os primeiros autocarros elétricos, da Caetano, chegaram em 2018.",
    "A linha 97 foi inaugurada a 15 de setembro de 2025, com o percurso Rua do Raio — Celeirós.",
    "A linha 98 foi inaugurada a 4 de novembro de 2024, com o percurso M. Arcos — Merelim São Pedro.",
    "A linha 501 foi inaugurada a 30 de agosto de 2021, com o percurso Avenida Central — Parque Industrial de Adaúfe.",
    "Em 2026, os AdB vão oferecer novas funcionalidades a todos os curiosos e entusiastas."
]

@app.route('/')
def manutencao():
    # Escolhe uma frase aleatória da lista acima
    curiosidade = random.choice(CURIOSIDADES_ADB)
    return render_template('manutencao.html', curiosidade=curiosidade)

@app.route('/linha/<numero>')
@app.route('/linha/<numero>/<ano>')
@app.route('/linha/<numero>/<ano>/<sentido>')
def detalhe_linha(numero, ano="2026", sentido="ida"):
    # ... (mantém o código da linha que já tínhamos)
    # Garante que chamas o carregar_linha e renderizas o linha.html
    pass

if __name__ == '__main__':
    # Usando a porta 5002 para evitar conflitos no teu Mac
    app.run(debug=True, port=5002)