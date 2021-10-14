from sprint5 import buscar_email, buscar_trecho_cpf, carregar_arquivo_csv_para_lista
from sprint5 import carregar_arquivo_txt_para_lista
from sprint5 import todos_arquivos_txt
from sprint5 import todos_arquivos_csv
from sprint5 import buscar_trecho_nome
from sprint5 import buscar_nome
from sprint5 import buscar_cpf
from sprint5 import buscar_trecho_cpf
from sprint5 import buscar_dominio_email
from sprint5 import buscar_trecho_nome_email
import pytest

def carrega_arquivo_csv():
    nome_arquivo = 'arquivos/diretorio5/arquivo_13.csv'
    return carregar_arquivo_csv_para_lista(nome_arquivo)

def carrega_arquivo_txt():
    nome_arquivo = 'arquivos/diretorio6/arquivo_1.txt'
    return carregar_arquivo_txt_para_lista(nome_arquivo)


class TestCarregarArquivos_para_lista:
    def test_carregar_arquivo_csv(self):
        arquivo = 'arquivos/diretorio5/arquivo_13.csv'
        sublista = carregar_arquivo_csv_para_lista(arquivo)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 250
        assert len(sublista[0]) == 3

    def test_carregar_arquivo_txt(self):
        arquivo = 'arquivos/diretorio2/arquivo_1.txt'
        sublista = carregar_arquivo_txt_para_lista(arquivo)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 250
        assert len(sublista[0]) == 3


class TestTodosArquivos:
    def test_todos_arquivos_txt(self):
        sublista = todos_arquivos_txt()
        assert isinstance(sublista, list)
        assert len(sublista) == 60

    def test_todos_arquivos_csv(self):
        sublista = todos_arquivos_csv()
        assert isinstance(sublista, list)
        assert len(sublista) == 120


class TestBuscarTrechoNome:
    def test_buscar_trecho_nome_1(self):
        lista = carrega_arquivo_txt()
        trecho_nome = 'Luz'
        sublista = buscar_trecho_nome(lista, trecho_nome)
        assert isinstance(sublista, list)
        assert len(sublista) == 7

    def test_buscar_trecho_nome_2(self):
        lista = carrega_arquivo_csv()
        trecho_nome = 'Luz'
        sublista = buscar_trecho_nome(lista, trecho_nome)
        assert isinstance(sublista, list)
        assert len(sublista) == 4


class TestBuscarNome:
    def test_buscar_nome_1(self):
        lista = carrega_arquivo_txt()
        nome_procurado = 'Matheus da Luz'
        sublista = buscar_nome(lista, nome_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1

    def test_buscar_nome_2(self):
        nome_procurado = 'Camila da Luz'
        lista = carrega_arquivo_csv()
        sublista = buscar_nome(lista, nome_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1


class TestBuscarCPF:
    def test_buscar_cpf_1(self):
        lista = carrega_arquivo_txt()
        cpf_procurado = '254.398.701-05'
        sublista = buscar_cpf(lista, cpf_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1

    def test_buscar_cpf_2(self):
        lista = carrega_arquivo_csv()
        cpf_procurado = '581.367.042-44'
        sublista = buscar_cpf(lista, cpf_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1


class TestBuscarTrechoCPF:
    def test_buscar_trecho_cpf_1(self):
        lista = carrega_arquivo_txt()
        cpf_procurado = '398'
        sublista = buscar_trecho_cpf(lista, cpf_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 2

    def test_buscar_trecho_cpf_2(self):
        lista = carrega_arquivo_csv()
        cpf_procurado = '581'
        sublista = buscar_trecho_cpf(lista, cpf_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 3



class TestBuscarEmail:
    def test_buscar_email_1(self):
        lista = carrega_arquivo_txt()
        email_procurado = 'luana80@ig.com.br'
        sublista = buscar_email(lista, email_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1

    def test_buscar_email_2(self):
        lista = carrega_arquivo_csv()
        email_procurado = 'camposjoao-pedro@bol.com.br'
        sublista = buscar_email(lista, email_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 1


class TestBuscarDominioEmail:
    def test_buscar_dominio_email_1(self):
        lista = carrega_arquivo_txt()
        dominio_procurado = 'ig.com.br'
        sublista = buscar_dominio_email(lista, dominio_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 14

    def test_buscar_dominio_email_2(self):
        lista = carrega_arquivo_csv()
        dominio_procurado = 'ig.com.br'
        sublista = buscar_dominio_email(lista, dominio_procurado)
        assert isinstance(sublista, list)
        assert len(sublista) == 20


class TestBuscar_TrechoNome_Email:
    def test_buscar_trechoNome_Email_1(self):
        lista = carrega_arquivo_csv()
        trecho_nome = 'Silva'
        email = 'franciscobarbosa@nascimento.br'
        sublista = buscar_trecho_nome_email(lista, trecho_nome, email)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1

    def test_buscar_trechoNome_Email_2(self):
        lista = carrega_arquivo_csv()
        trecho_nome = 'Duarte'
        email = 'franciscobarbosa@nascimento.br'
        sublista = buscar_trecho_nome_email(lista, trecho_nome, email)
        assert isinstance(sublista, list)
        assert len(sublista) == 0
