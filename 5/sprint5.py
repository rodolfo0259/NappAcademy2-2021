import os
import glob
import csv

def todos_arquivos_txt()->list:
    ''' Encontra todos os arquivos txt dentro da pasta e subpastas '''
    looking_for = '**/*.txt'
    matched = glob.glob(looking_for, recursive=True)
    return matched


def todos_arquivos_csv()->list:
    ''' Encontra todos os arquivos csv dentro da pasta e subpastas '''
    looking_for = '**/*.csv'
    matched = glob.glob(looking_for, recursive=True)
    return matched


def carregar_arquivo_txt_para_lista(nome_arquivo)->list:
    ''' Transforma o conteudo do arquivo txt em uma lista de tuplas '''
    lista = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n','')
            linha = linha.split('\t')
            linha = linha[0:-1]
            lista.append(tuple(linha))
    return lista


def carregar_arquivo_csv_para_lista(nome_arquivo)->list:
    ''' Transforma o conteudo do arquivo csv em uma lista de tuplas '''
    lista = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n','')
            linha = linha.split(',')
            # linha = linha[0:-1]
            lista.append(tuple(linha))
    return lista[1:]


def buscar_trecho_nome(lista, trecho_nome)->list:
    ''' Encontra todos os registros onde há o padrao string no campo 'Nome' e adiciona-os em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        trecho_nome: padrao string para ser encontrado na lista
    Return:
        Lista com tuples com registros encontrados
    '''
    sublista = list()
    for tupla in lista:
        if trecho_nome in tupla[0]:
            sublista.append(tupla)
    return sublista


def buscar_nome(lista, trecho_nome):
    ''' Encontra um nome especifico dentro da lista de tuples '''
    return buscar_trecho_nome(lista, trecho_nome)

def buscar_email(lista, email):
    ''' Encontra todos os registros onde há o padrao string no campo 'Nome' e adiciona-os em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        trecho_nome: padrao string para ser encontrado na lista
    Return:
        Lista com tuples com registros encontrados
    '''
    sublista = list()
    for tupla in lista:
        if email in tupla[2]:
            sublista.append(tupla)
    return sublista

def buscar_cpf(lista, cpf):
    ''' Encontra todos os registros onde há o padrao string no campo 'Nome' e adiciona-os em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        trecho_nome: padrao string para ser encontrado na lista
    Return:
        Lista com tuples com registros encontrados
    '''
    sublista = list()
    for tupla in lista:
        if cpf in tupla[1]:
            sublista.append(tupla)
    return sublista

def buscar_trecho_cpf(lista, trecho_cpf):
    return buscar_cpf(lista, trecho_cpf)

def buscar_dominio_email(lista, dominio):
    return buscar_email(lista, dominio)

def buscar_trecho_nome_email(lista, trecho_nome, email):
    ''' Encontra todos os registros onde há o padrao string no campo 'Nome' e adiciona-os em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        trecho_nome: padrao string para ser encontrado na lista
    Return:
        Lista com tuples com registros encontrados
    '''
    sublista = list()
    for tupla in lista:
        if trecho_nome in tupla[0] and email in tupla[2]:
            sublista.append(tupla)
    return sublista


def gravar_lista_para_arquivo_csv(lista, nome_arquivo):
    with open(nome_arquivo,'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(['Nome', 'CPF', 'E-mail'])
        wr.writerows(lista)

'''
if __name__ == '__main__':
    root_dir = os.getcwd()
    new_dir = os.getcwd() + '/arquivos/'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_1 = buscar_dominio_email(ocorrencias, 'ig.com.br')

    os.chdir(root_dir)    
    new_dir = os.getcwd() + '/arquivos/diretorio6'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_2 = buscar_dominio_email(ocorrencias, 'ig.com.br')
    
    # NESTE TRECHO, ALTERAR O DIRETÓRIO DE TRABALHO
    # Os arquivos gerados com as funções abaixo devem gerar arquivos
    # dentro do diretório relatorio. Este diretório deve ser criado via script também
    
    gravar_lista_para_arquivo_csv(dominio_ig_1, 'dominio_ig_all.csv')
    gravar_lista_para_arquivo_csv(dominio_ig_2, 'dominio_ig_dir6.csv')
'''

print(buscar_trecho_nome([('aac', 'something', 'anything')], 'abc'))