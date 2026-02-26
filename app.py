from flask import Flask, render_template, request, jsonify
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'web'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/minerar', methods=['POST'])
def minerar():
    dados = request.get_json()
    nicho = dados.get('nicho')
    plataforma = dados.get('plataforma')

    # Simulando a inteligência da ferramenta
    # Aqui é onde o seu bot/IA realmente trabalha
    resumo_mineracao = {
        "status": "sucesso",
        "tendencias": [
            f"Como crescer com {nicho} em 2026",
            f"O segredo dos fornecedores de {nicho}",
            f"Review de ferramentas para {nicho}"
        ],
        "prompt": f"Atue como um especialista em {plataforma}. Crie um roteiro viral focado no nicho de {nicho}, usando as ferramentas CapCut e a estratégia de retenção de 3 segundos."
    }
    
    return jsonify(resumo_mineracao)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
