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


def find_pattern(lista: list, patterns: dict)->list:
    ''' 
    Encontra todos os registros onde há o padrao string fornecido e 
    ira adiciona-los em uma lista 
    Args:
        lista: uma lista de tuplas contem os registros
        patterns: 
            dicionario com a posicao da coluna/campo e 
            padrao string para ser encontrado no determinado campo
    Return:
        Lista com tuples com registros encontrados
    '''
    pattern_list = [None, None, None]
    for i in list(patterns.keys()):
        pattern_list[i] = patterns[i]

    truth_tuple = [bool(x) for x in pattern_list]

    match_list = list()
    for item in lista:
        temp_contain = list()
        for i in range(len(truth_tuple)):
            if truth_tuple[i]:
                if pattern_list[i] in item[i]:
                    temp_contain.append(True)
            else:
                temp_contain.append(False)

        if temp_contain == truth_tuple:
            match_list.append(item)
    
    return match_list


def buscar_trecho_nome(lista, trecho_nome)->list:
    return find_pattern(lista, {0: trecho_nome})


def buscar_cpf(lista, cpf)->list:
    return find_pattern(lista, {1: cpf})


def buscar_email(lista, email)->list:
    return find_pattern(lista, {2: email})


def buscar_trecho_nome_email(lista, trecho_nome, email)->list:
    return find_pattern(lista, {0: trecho_nome, 2: email})


''' funcoes com nomes diferentes, porem mesma funcionalidade '''
buscar_nome = buscar_trecho_nome
buscar_trecho_cpf = buscar_cpf
buscar_dominio_email = buscar_email


def gravar_lista_para_arquivo_csv(lista: list, nome_arquivo: str)->None:
    '''
    Ira transformar a lista em um arquivos csv no caminho especificado
    por padrao dentro de ./relatorios
    Args:
        lista: lista de tuples
        nome_arquivo: caminho com nome do arquivo
    '''
    with open(nome_arquivo,'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(['Nome', 'CPF', 'E-mail'])
        wr.writerows(lista)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))

    new_dir = current_path + '/arquivos/'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_1 = buscar_dominio_email(ocorrencias, 'ig.com.br')

    os.chdir(current_path)    
    new_dir = current_path + '/arquivos/diretorio6'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_2 = buscar_dominio_email(ocorrencias, 'ig.com.br')
    
    if not os.path.isdir(f'{current_path}/relatorio'):
        os.mkdir(f'{current_path}/relatorio')

    gravar_lista_para_arquivo_csv(dominio_ig_1, f'{current_path}/relatorio/dominio_ig_all.csv')
    gravar_lista_para_arquivo_csv(dominio_ig_2, f'{current_path}/relatorio/dominio_ig_dir6.csv')
