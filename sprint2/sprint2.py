import csv
import datetime
         
def carregar_arquivo_para_lista(nome_arquivo)->list:
    """
    Função recebe o nome de um arquivo csv e retorna a lista 
    de tuplas

    Args:
        nome_arquivo (string): Nome do arquivo CSV

    Returns:
        list: Lista com tuplas
    """
    lista = []
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lista.append(tuple(row))
    lista = lista[1:]
    return lista


def carregar_arquivos_para_lista(*lista_arquivos)->list:
    """
    Função recebe nomes de arquivos csv e retorna a lista 
    de tuplas com 

    Args:
        lista_arquivos (tuple): Contem nome dos arquivos CSV

    Return:
        list: Uma lista com dados, de cada csv, em tuplas
    """
    lista = []
    for name in lista_arquivos:
        with open(name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip header
            for row in reader:
                lista.append(tuple(row))
        # lista = lista[1:] #skip header ?
    return lista


def busca_mes_vencimento_cartao_credito(lista, **parametros)->list:
    '''
    Busca registros na lista de tuples que contenham a data de vencimento do cartao,
    no valor mes/ano fornecido ou o padrao 23/03 caso omitido

    Args:
        lista: lista de tuples (obrigatorio)
        parametros: mes e ano (opcional)

    Return:
        list: lista de tuples com registros filtrados pelo mes/ano
    '''
    lis = list()
    parametros = {
        'ano': '23',
        'mes': '03',
        **parametros
        }
    for item in lista:
        if parametros['mes']+'/'+parametros['ano'] in item[-1]:
            lis.append(item)
    
    return lis


def contar_ocorrencias_cartao_credito_por_mes(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada mes

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict: dicionario contendo o mes e a quatidade de ocorrencias para cada
    '''
    count = dict()
    for item in lista:
        mes = item[-1].split('/')[0]
        if mes in count:
            count[mes] += 1
        else:
            count[mes] = 1
 
    return count


def contar_ocorrencias_cartao_credito_por_ano(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada ano

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict: dicionario contendo o ano e a quatidade de ocorrencias para cada
    '''
    count = dict()
    for item in lista:
        ano = item[-1].split('/')[1]
        if ano in count:
            count[ano] += 1
        else:
            count[ano] = 1
 
    return count


def busca_cvc(lista, cvc='043')->list:
    '''
    Encontrar todos os registros cujo codigo de verificacao do cartao(cvc)
    seja igual ao fornecido, caso omitido sera por padrao 043

    Args:
        lista: lista de tuples (obrigatorio)
        cvc: numero em string

    Return:
        list: lista com registros encontrados
    '''
    lis = list()
    pattern = f'CVC: {cvc}'
    for item in lista:
        if pattern in item[-2]:
            lis.append(item)
 
    return lis


def busca_lista_cvcs(lista, *cvcs)->list:
    '''
    Encontrar todos os registros cujo os codigos de verificacao do cartao(cvc)
    sejam igual aos fornecidos, caso omitido sera por padrao 043

    Args:
        lista: lista de tuples (obrigatorio)
        cvc: numero em string ou tuple

    Return:
        list: lista com todos os registros encontrados
    '''
    if len(cvcs) == 0:
        cvcs = ('043',)
    lis = list()
    for cvc in cvcs:
        pattern = f'CVC: {cvc}'
        for item in lista:
            if pattern in item[-2]:
                lis.append(item)
                lista.remove(item) # remove already found item
 
    return lis


def contar_ocorrencias_por_estado(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada estado

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict: dicionario contendo o estado e a quatidade de ocorrencias para cada
    '''
    count = dict()
    for item in lista:
        uf = (item[-3].split('/')[-1]).strip()
        if uf in count:
            count[uf] += 1
        else:
            count[uf] = 1
 
    return count


def busca_dados_navegador(lista, navegador='Chrome/24')->list:
    '''
    Encontra todos os registros que contenham dados de navegador 
    iguais aos fornecidos, caso omitido sera por padrao Chrome/24

    Args:
        lista: lista de tuples (obrigatorio)
        navegador: string para pesquisa do navegador (opcional)

    Return:
        list: lista com todos os registros encontrados
    '''
    lis = list()
    for item in lista:
        if navegador in item[-4]:
            lis.append(item)
 
    return lis


def contar_ocorrencias_por_sufixo_dominio(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao
    para cada sufixo de dominio de website

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict: dicionario contendo o dominio de cada website
        e a quatidade de ocorrencias para cada
    '''
    count = dict()
    for item in lista:
        sufixo = (item[4].split('.')[-1]).strip()
        if sufixo in count:
            count[sufixo] += 1
        else:
            count[sufixo] = 1
 
    return count


def contar_ocorrencias_por_dominio_email(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada dominio de email

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict: dicionario contendo o dominio de cada email
        e a quatidade de ocorrencias para cada
    '''
    count = dict()
    for item in lista:
        dominio = (item[2].split('@')[-1]).strip()
        if dominio in count:
            count[dominio] += 1
        else:
            count[dominio] = 1
 
    return count


def buscar_dominio_mais_utilizado(lista)->tuple:
    '''
    Conta a maior ocorrencia de email de fraude de cartao

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        tuple: contendo o email mais usado e quantidade de registros onde ocorre
    '''
    count = dict()
    for item in lista:
        dominio = (item[2].split('@')[-1]).strip()
        if dominio in count:
            count[dominio] += 1
        else:
            count[dominio] = 1
    
    popular = max(count, key=count.get)
    popular = (popular, count[popular])

    return popular


def contar_ocorrencias_por_semana(lista)->list:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada dia da semana

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        lista de tuples com o dia da semana e o total de ocorrencias
    '''
    week_day = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    count = dict()
    for item in lista:
        data = item[3]
        dia_semana = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S").weekday()
        if dia_semana in count:
            count[dia_semana] += 1
        else:
            count[dia_semana] = 1
 
    for i in range(7):
        count[week_day[i]] = count.pop(i)

    lis = [(k, v) for k, v in count.items()]

    return lis


def contar_ocorrencias_por_hora(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada hora registrada

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict com cada hora e o total de ocorrencias
    '''
    count = dict()
    for item in lista:
        data = item[3]
        hora = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S").hour
        hora = '{:02d}'.format(hora)
        if hora in count:
            count[hora] += 1
        else:
            count[hora] = 1

    return count


def contar_ocorrencias_por_mes(lista)->dict:
    '''
    Conta todas as ocorrencias de fraude de cartao para cada mes

    Args:
        lista: lista de tuples (obrigatorio)

    Return:
        dict com cada mes e o total de ocorrencias
    '''
    count = dict()
    for item in lista:
        data = item[3]
        mes = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S").month
        mes = '{:02d}'.format(mes)
        if mes in count:
            count[mes] += 1
        else:
            count[mes] = 1

    return count


if __name__ == "__main__":
    lista = carregar_arquivo_para_lista('arquivo_1.csv')