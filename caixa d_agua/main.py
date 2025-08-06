from flask import Flask, jsonify, request,render_template
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    conn = sqlite3.connect("nivel_agua.db")
    cursor = conn.cursor()
    cursor.execute("SELECT valor FROM niveis ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    nivel_atual = int(float(row[0])) if row else 0  # Se ele não achar nenhum valor, mostra 0
    return render_template('index.html', nivel_atual=nivel_atual)

@app.route("/nivel", methods=["POST"])
def salvar_nivel():
    valor = request.json.get("valor")
    if valor is None:
        return jsonify({"erro": "valor não informado"}), 400

    try:
        conn = sqlite3.connect("nivel_agua.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO niveis (valor) VALUES (?)", (valor,))
        conn.commit()
        conn.close()
        print(f"Nível salvo no banco: {valor}")
        return jsonify({"status": "nível salvo"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500



@app.route("/historico", methods=["GET"])
def historico():
    conn = sqlite3.connect("nivel_agua.db")
    cursor = conn.cursor()
    cursor.execute("SELECT valor, timestamp FROM niveis ORDER BY timestamp DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"valor": r[0], "timestamp": r[1]} for r in rows])


@app.route("/comando", methods=["POST"])
def comando():
    acao = request.json.get("acao")
    
    if acao not in ["ligar", "desligar"]:
        print("Comando inválido recebido!")  # <-- print de erro
        return jsonify({"erro": "comando inválido"}), 400

    print(f"Bomba: {acao.upper()}")  # pra imprimir o comando no terminal
    
    conn = sqlite3.connect("nivel_agua.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comando (acao) VALUES (?)", (acao,))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "comando recebido", "acao": acao})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
