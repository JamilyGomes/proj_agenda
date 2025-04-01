import json
import os
from datetime import datetime
import hashlib

ARQUIVO_DADOS = "usuarios.json"

def inicializar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        dados = {"usuarios": [], "mensagens": []}
        with open(ARQUIVO_DADOS, "w") as f:
            json.dump(dados, f, indent=4)

def carregar_dados():
    inicializar_dados()
    with open(ARQUIVO_DADOS, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)

def salvar_usuario(nome, email, contato, senha, foto=None):
    dados = carregar_dados()
    for usuario in dados["usuarios"]:
        if usuario["email"] == email:
            print(f"Erro: Email {email} já está registrado.")
            return False
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    novo_usuario = {
        "id": len(dados["usuarios"]) + 1,
        "nome": nome,
        "email": email,
        "contato": contato,
        "senha_hash": senha_hash,
        "foto": foto.hex() if foto else None
    }
    dados["usuarios"].append(novo_usuario)
    salvar_dados(dados)
    print(f"Usuário {nome} salvo com sucesso.")
    return True

def autenticar_usuario(email, senha):
    dados = carregar_dados()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    for usuario in dados["usuarios"]:
        if usuario["email"] == email and usuario["senha_hash"] == senha_hash:
            return True, usuario["id"], usuario["nome"]
    return False, None, None

def obter_usuarios():
    dados = carregar_dados()
    return [{"id": u["id"], "nome": u["nome"]} for u in dados["usuarios"]]

def salvar_mensagem(remetente_id, destinatario_id, mensagem):
    dados = carregar_dados()
    nova_mensagem = {
        "id": len(dados["mensagens"]) + 1,
        "remetente_id": remetente_id,
        "destinatario_id": destinatario_id,
        "mensagem": mensagem,
        "data_envio": datetime.now().isoformat()
    }
    dados["mensagens"].append(nova_mensagem)
    salvar_dados(dados)
    print(f"Mensagem salva: {mensagem}")
    return True

def obter_mensagens(usuario_id, outro_usuario_id):
    dados = carregar_dados()
    mensagens = [
        m for m in dados["mensagens"]
        if (m["remetente_id"] == usuario_id and m["destinatario_id"] == outro_usuario_id) or
           (m["remetente_id"] == outro_usuario_id and m["destinatario_id"] == usuario_id)
    ]
    return sorted(mensagens, key=lambda x: x["data_envio"])

if __name__ == "__main__":
    inicializar_dados()