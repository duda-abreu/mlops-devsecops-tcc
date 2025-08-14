# Vulnerabilidade 1: uso de eval
def unsafe_eval(user_input):
    return eval(user_input)  # Bandit vai detectar

# Vulnerabilidade 2: subprocess sem validação
import subprocess
def unsafe_subprocess():
    subprocess.call("ls /", shell=True)  # inseguro

# Vulnerabilidade 3: senha hardcoded
PASSWORD = "123456"  # Bandit detecta hardcoded secret
