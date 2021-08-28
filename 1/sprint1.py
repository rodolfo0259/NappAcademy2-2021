import pickle 
         
def prefixo_dr_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR'):
            sublista.append(item)
    return sublista # poderiamos retornar a len() tambem

def total_prefixo_dr_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR'):
            total = total + 1
    return total

def prefixo_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DRA'):
            sublista.append(item[0])
    return sublista # poderiamos retornar a len() tambem

def total_prefixo_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DRA'):
            total = total + 1
    return total

def prefixo_dr(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR.'):
            sublista.append(item[0])
    return sublista # poderiamos retornar a len() tambem

def total_prefixo_dr(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR.'):
            total = total + 1
    return total

def busca_sobrenomes(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome in (item[0]).split(' ')[-1]:
            sublista.append((item[0:2]))
    return sublista

def busca_sobrenomes_primeiros(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome in (item[0]).split(' ')[-1]:
            sublista.append((item[0:2]))
        if len(sublista) == 10:
            return sublista

def busca_sobrenomes_ultimos(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome in (item[0]).split(' ')[-1]:
            sublista.append((item[0:2]))
    return sublista[-10:]

def busca_email(lista, email):
    for item in lista:
        if email in item[2]:
            return (item)
    return ()

def busca_email_por_dominio(lista, dominio='gmail.com'):
    sublista = []
    for item in lista:
        if dominio in item[2]:
            sublista.append(item)
    return sublista

def busca_email_por_usuario(lista, username):
    sublista = []
    for item in lista:
        if username in item[2]:
            sublista.append(item)
    return sublista

def busca_endereco(lista, endereco):
    sublista = []
    for item in lista:
        if endereco in item[7]:
            sublista.append(item)
    return sublista

def busca_estado(lista):
    sublista = []
    for item in lista:
            sublista.append((item[7]).split(' ')[-1])
    return list(set(sublista))

def busca_cartao_credito(lista, numero_cartao_procurado):
    sublista = []
    for item in lista:
        if numero_cartao_procurado in item[8]:
            sublista.append(item)
    return sublista

def busca_vencimento_cartao_credito(lista, mes_ano_vencimento):
    sublista = []
    for item in lista:
        if mes_ano_vencimento in item[9]:
            sublista.append(item)
    return sublista

def busca_mes_vencimento_cartao_credito(lista, mes_vencimento):
    sublista = []
    for item in lista:
        if str(mes_vencimento) in item[9].split('/')[0]:
            sublista.append(item)
    return sublista

def busca_ip(lista, ip_procurado):
    sublista = []
    for item in lista:
        if str(ip_procurado) in item[5]:
            sublista.append(item)
    return sublista

def busca_prefixo_ip(lista, prefixo_ip='192'):
    sublista = []
    for item in lista:
        if str(prefixo_ip) in item[5].split('.')[0]:
            sublista.append(item)
    return sublista

def busca_prefixo_sufixo_ip(lista, prefixo_ip='192', sufixo_ip='0'):
    sublista = []
    for item in lista:
        if prefixo_ip in item[5].split('.')[0] and (('.'+sufixo_ip) in '.'+(item[5].split('.')[-1])):
            sublista.append(item)
    return sublista

if __name__ == "__main__":
    with open('lista.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
