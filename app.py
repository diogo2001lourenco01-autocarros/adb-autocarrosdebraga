from flask import Flask, render_template

app = Flask(__name__)

# Rota principal - Temporariamente a apontar para a manutenção
@app.route('/')
def index():
    # Quando o site real estiver pronto, mudas isto de volta para 'index.html'
    return render_template('manutencao.html')

if __name__ == '__main__':
    # Esta linha é importante para o Render correr no ambiente de produção
    # mas o Gunicorn no Render trata disso. Isto é mais para testes locais.
    app.run()