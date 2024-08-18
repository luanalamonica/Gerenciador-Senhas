from cryptography.fernet import Fernet
import json
import os

# Gerar e armazenar uma chave de criptografia
def generate_key():
    return Fernet.generate_key()

def load_key():
    if os.path.exists("secret.key"):
        return open("secret.key", "rb").read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Funções de criptografia
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# Gerenciar senhas
class PasswordManager:
    def __init__(self):
        self.key = load_key()
        self.file = "passwords.json"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def add_password(self, site, password):
        encrypted_password = encrypt_password(password, self.key)
        with open(self.file, "r") as f:
            data = json.load(f)
        data[site] = encrypted_password.decode()
        with open(self.file, "w") as f:
            json.dump(data, f)

    def get_password(self, site):
        with open(self.file, "r") as f:
            data = json.load(f)
        encrypted_password = data.get(site)
        if encrypted_password:
            return decrypt_password(encrypted_password.encode(), self.key)
        return None

    def delete_password(self, site):
        with open(self.file, "r") as f:
            data = json.load(f)
        if site in data:
            del data[site]
            with open(self.file, "w") as f:
                json.dump(data, f)

    def list_sites(self):
        with open(self.file, "r") as f:
            data = json.load(f)
        return list(data.keys())
