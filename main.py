import pandas as pd
import streamlit as st

USUARIOS_PATH = "db/usuarios.csv"
DADOS_PATH = "db/dados_reciclagem.csv"

def carregar_csv(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        return pd.DataFrame()

def salvar_csv(caminho, df):
    df.to_csv(caminho, index=False)

def validar_usuario(email, senha):
    usuarios = carregar_csv(USUARIOS_PATH)
    usuario = usuarios[(usuarios['email'] == email) & (usuarios['senha'] == senha)]
    return not usuario.empty

def cadastrar_usuario(nome, email, senha):
    usuarios = carregar_csv(USUARIOS_PATH)
    novo_usuario = {"nome": nome, "email": email, "senha": senha}
    usuarios = usuarios.append(novo_usuario, ignore_index=True)
    salvar_csv(USUARIOS_PATH, usuarios)

def registrar_reciclagem(usuario_id, tipo_residuo, peso):
    dados = carregar_csv(DADOS_PATH)
    novo_dado = {"usuario_id": usuario_id, "tipo_residuo": tipo_residuo, "peso": peso}
    dados = dados.append(novo_dado, ignore_index=True)
    salvar_csv(DADOS_PATH, dados)