import os
import glob
import csv

def find_all_files(extension)->list:
    ''' Encontra todos os arquivos de determinada extensao dentro da pasta e subpastas '''
    looking_for = f'**/*.{extension}'
    matched = glob.glob(looking_for, recursive=True)
    return matched


def todos_arquivos_txt()->list:
    return find_all_files('txt')


def todos_arquivos_csv()->list:
    return find_all_files('csv')


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


def find_pattern(lista: list, string_pattern: str, column_index: int)->list:
    ''' Encontra todos os registros onde há o padrao string e ira adiciona-los em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        string_pattern: padrao string para ser encontrado na lista
        column_index: numero da coluna/campo onde o padrao deve ser procurado
    Return:
        Lista com tuples com registros encontrados
    '''
    sublista = list()
    for tupla in lista:
        if string_pattern in tupla[column_index]:
            sublista.append(tupla)
    return sublista


def buscar_trecho_nome(lista, trecho_nome)->list:
    return find_pattern(lista, trecho_nome, 0)


def buscar_cpf(lista, cpf)->list:
    return find_pattern(lista, cpf, 1)


def buscar_email(lista, email)->list:
    return find_pattern(lista, email, 2)


''' funcoes com nomes diferentes, porem mesma funcionalidade '''
buscar_nome = buscar_trecho_nome
buscar_trecho_cpf = buscar_cpf
buscar_dominio_email = buscar_email


def buscar_trecho_nome_email(lista, trecho_nome, email)->list:
    ''' Encontra todos os registros onde há o padrao string no campo 'Nome' e no campo email
    e ira adiciona-los em uma lista 
    Args:
        lista: uma lista de tuples contem os registros
        trecho_nome: padrao string do nome a ser encontrado
        email: padrao string de email a ser encontrado
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