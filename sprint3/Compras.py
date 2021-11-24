from DAO import DAO
from Registro import Registro
import csv


class Compras:
    def __init__(self, nome_banco_dados):
        self.nome_banco_dados = nome_banco_dados
        conexao_banco = DAO(self.nome_banco_dados)
        self._registros = []
        for item in conexao_banco.get_registros_todos():
            registro = Registro(item)
            self._registros.append(registro)
        conexao_banco.close()


    def localizar_compras_no_dia_mes(self, dia, mes)->list:
        lista_retorno = []
        for registro in self._registros:
            if registro.comprado_no_dia_mes(dia, mes):
                lista_retorno.append(registro)
        return lista_retorno


    def localizar_compras_por_produto(self, produto)->list:
        reg_lista = list()
        conexao_banco = DAO(self.nome_banco_dados)
        for item in conexao_banco.get_registros_por_produto(produto):
            registro = Registro(item)
            reg_lista.append(registro)
        conexao_banco.close()
        return reg_lista


    def localizar_compras_por_preco(self, preco_minimo, preco_maximo)->list:
        reg_lista = list()
        conexao_banco = DAO(self.nome_banco_dados)
        for item in conexao_banco.get_registros_preco(preco_minimo, preco_maximo):
            registro = Registro(item)
            reg_lista.append(registro)
        conexao_banco.close()
        return reg_lista


    def gravar_para_arquivo_csv(self, nome_arquivo):
        campos = ('id', 'Produto', 'Preço', 'Quantidade', 'data')
        with open(nome_arquivo + '.csv', 'w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerow(campos)
            for compra in self._registros:
                wr.writerow(compra.get_tupla())


    def __str__(self):
        return 'Lista de compras extraída do banco de dados ' + self.nome_banco_dados


    def __repr__(self):
        return 'Lista de compras extraída do banco de dados ' + self.nome_banco_dados

