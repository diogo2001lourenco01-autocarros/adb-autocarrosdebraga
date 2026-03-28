from flask import Flask, render_template
import os

# Configuração rigorosa para garantir que o Flask encontra os ficheiros no Mac
app = Flask(__name__, 
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # O debug=True ajuda a ver erros no terminal se a fonte falhar
    app.run(debug=True, port=5000)