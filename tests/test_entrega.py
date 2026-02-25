"""
Testes automatizados para validação da entrega dos desafios.

Este arquivo contém testes que verificam se os arquivos de solução foram
criados, se contêm código válido e se foram implementados pelo aluno.
"""

import os
import ast
import pytest

# Lista dos arquivos de desafio esperados
ARQUIVOS_DESAFIOS = [
    'desafio_1001.py',
    'desafio_1002.py',
    'desafio_1003.py',
    'desafio_1004.py',
    'desafio_1005.py'
]

# Diretório raiz do projeto (um nível acima de tests/)
DIRETORIO_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_arquivos_existem():
    """
    Verifica se todos os arquivos de desafio existem no diretório raiz.
    """
    for arquivo in ARQUIVOS_DESAFIOS:
        caminho_arquivo = os.path.join(DIRETORIO_RAIZ, arquivo)
        assert os.path.exists(caminho_arquivo), \
            f"Arquivo '{arquivo}' não encontrado no diretório raiz"


def test_arquivos_nao_vazios():
    """
    Verifica se cada arquivo contém mais de 10 caracteres,
    indicando que o aluno escreveu algo além do template básico.
    """
    for arquivo in ARQUIVOS_DESAFIOS:
        caminho_arquivo = os.path.join(DIRETORIO_RAIZ, arquivo)

        # Verifica se o arquivo existe antes de ler
        if not os.path.exists(caminho_arquivo):
            pytest.skip(f"Arquivo '{arquivo}' não encontrado")

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        assert len(conteudo) > 10, \
            f"Arquivo '{arquivo}' está muito pequeno. Você implementou a solução?"


def test_codigo_valido():
    """
    Verifica se cada arquivo contém código Python sintaticamente válido
    usando ast.parse().
    """
    for arquivo in ARQUIVOS_DESAFIOS:
        caminho_arquivo = os.path.join(DIRETORIO_RAIZ, arquivo)

        # Verifica se o arquivo existe antes de ler
        if not os.path.exists(caminho_arquivo):
            pytest.skip(f"Arquivo '{arquivo}' não encontrado")

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()

        try:
            ast.parse(codigo)
        except SyntaxError as e:
            pytest.fail(f"Erro de sintaxe no arquivo '{arquivo}': {e}")


def test_tem_input_ou_print():
    """
    Verifica se cada arquivo usa input() ou print(), indicando que
    é uma solução real e não apenas o template.
    """
    for arquivo in ARQUIVOS_DESAFIOS:
        caminho_arquivo = os.path.join(DIRETORIO_RAIZ, arquivo)

        # Verifica se o arquivo existe antes de ler
        if not os.path.exists(caminho_arquivo):
            pytest.skip(f"Arquivo '{arquivo}' não encontrado")

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()

        # Verifica se contém input() ou print()
        tem_input = 'input(' in codigo
        tem_print = 'print(' in codigo

        assert tem_input or tem_print, \
            f"Arquivo '{arquivo}' não contém input() ou print(). Você implementou a solução?"
