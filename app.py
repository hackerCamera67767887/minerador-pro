from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/minerar', methods=['POST'])
def minerar():
    dados = request.json
    plataforma = dados.get('plataforma')
    nicho = dados.get('nicho')
    
    # Aqui o servidor chama seus scripts Python de mineração
    # Por enquanto, devolvemos um status de sucesso
    return jsonify({
        "status": "sucesso",
        "mensagem": f"Mineração iniciada em {plataforma} para o nicho {nicho}",
        "resultado": f"Tendências de {nicho} encontradas!"
    })

if __name__ == '__main__':
    print("🚀 Servidor rodando em http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
