from flask import Flask, request, jsonify
import subprocess
import pickle
import os

app = Flask(__name__)

# Vulnerabilidade SECRET_KEY hardcoded
app.config['SECRET_KEY'] = 'chave_secreta_teste_123'

# Vulnerabilidade credencial hardcoded
ADMIN_PASSWORD = "admin1234"

@app.route("/Health")
def health():
    return jsonify({"status": "ok"})

@app.route("/run_eval", methods=["POST"])
def run_eval():
    # Vulnerabilidade: executa eval em conteúdo do usuário
    payload = request.data.decode('utf-8') or "0"
    try:
        result = eval(payload)
    except Exception as e:
        result = {"error": str(e)}
    return jsonify({"result": str(result)})

@app.route("/exec", methods=["POST"])
def exec_cmd():
    # Vulnerabilidade: subprocess com shell=True a partir de input
    cmd = request.args.get("cmd", "echo hello")
    subprocess.call(cmd, shell=True)
    return jsonify({"executed": cmd})

@app.route("/load_pickle", methods=["POST"])
def load_pickle():
    # Vulnerabilidade: desserialização insegura de dados enviados pelo cliente
    data = request.data
    try:
        obj = pickle.loads(data) 
        return jsonify({"loaded": True})
    except Exception as e:
        return jsonify({"loaded": False, "error": str(e)})

if __name__ == "__main__":
    app.run(port=5000)
