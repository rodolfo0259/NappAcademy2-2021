import csv

class Sprint2:
    def __init__(self):
        self.lista = list()
        

    def carregar_arquivo_para_lista(self, nome_arquivo: str):
        '''
        Função recebe o nome de um arquivo csv e retorna uma lista 
        de tuplas com seus registros nao repetidos

        Args:
            nome_arquivo (string): Nome do arquivo CSV
        '''
        with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if tuple(row) not in self.lista:
                    self.lista.append(tuple(row))


    def busca_trecho_nome(self, nome: str)->list:
        '''
        Encontrar todos os nomes que contenham padrao fornecido

        Args:
            str: padrao no campo nome a ser encontrado (obrigatorio)
        '''
        lis = list()
        for item in self.lista:
            if nome in item[0]:
                lis.append((item[0], item[1]))
        
        return lis
    

    def busca_email(self, email: str)->tuple:
        '''
        Encontrar o email fornecido

        Args:
            email: string contendo o email a ser procurado (obrigatorio)
        '''
        for item in self.lista:
            if email in item[2]:
                return tuple(item)
        
        return tuple()
        

    def busca_estado(self)->list:
        '''
        Encontra todos os estados(uf)
        '''
        lis = list()
        for item in self.lista:
            uf = (item[-3].split('/')[-1]).strip()
            lis.append(uf)

        return list(set(lis))
        
 
    def busca_mes_vencimento_cartao_credito(self, mes_vencimento: str)->list:
        '''
        Encontra todas as ocorrencias de fraude de cartao para cada mes

        Args:
            mes_vencimento: mes de vencimento do cartao (obrigatorio)

        Return:
            lista com cada registro onde houve ocorrencias
        '''
        lis = list()
        for item in self.lista:
            if mes_vencimento == item[-1].split('/')[0]:
                lis.append(item)
        
        return lis


    def busca_prefixo_sufixo_ip(self, prefixo_ip: str='192', sufixo_ip: str='0')->list:
        '''
        Encontra todas as ocorrencias de fraude onde o ip possua
        o prefixo e sufixo, caso omitido, por padrao sera
        prefixo = 192 e sufixo = 0

        Args:
            prefixo_ip: string (opcional)
            sufixo_ip: string (opcional)

        Return:
            lista com cada registro onde houve ocorrencias
        '''
        lis = list()
        for item in self.lista:
            if prefixo_ip == item[5].split('.')[0] and sufixo_ip == (item[5].split('.')[-1]):
                lis.append(item)
        
        return lis


    def contar_ocorrencia_por_dominio_hostname(self, *dominios)->list:
        '''
        Conta todas as ocorrencias de cada de dominio fornecido

        Args:
            dominios: string em tuple com os dominios (obrigatorio)

        Return:
            lista de tuples contendo o dominio
            e a quatidade de ocorrencias para cada
            Caso nao tenha, retorna dominio procurado, com zero ocorrencias
        '''
        final_lis = list()
        lis = list()
        count = dict()
        for item in self.lista:
            dominio = '.'.join(item[4].split('.')[-2:])
            if dominio in count:
                count[dominio] += 1
            else:
                count[dominio] = 1

        lis = [(k, v) for k, v in count.items()]

        for string in dominios:
            existe = False
            for item in lis:
                if string == item[0]:
                    final_lis.append(item)
                    existe = True
                    break
            
            if not existe:
                final_lis.append((string, 0))
            
        return final_lis
 

    def contar_ocorrencia_por_dominio_email(self, *dominios)->list:
        '''
        Conta todas as ocorrencias de cada de dominio email fornecido

        Args:
            dominios: string em tuple com os dominios (obrigatorio)

        Return:
            lista de tuples contendo o dominio de email
            e a quatidade de ocorrencias para cada
            Caso nao tenha, retorna dominio procurado, com zero ocorrencias
        '''
        final_lis = list()
        lis = list()
        count = dict()
        for item in self.lista:
            dominio = (item[2].split('@')[-1])
            if dominio in count:
                count[dominio] += 1
            else:
                count[dominio] = 1

        lis = [(k, v) for k, v in count.items()]

        for string in dominios:
            existe = False
            for item in lis:
                if string == item[0]:
                    final_lis.append(item)
                    existe = True
                    break
            
            if not existe:
                final_lis.append((string, 0))
            
        return final_lis

 
    def busca_mes_aniversario(self, mes_aniversario)->list:
        '''
        Busca registros na lista de tuples que contenham o mes fornecido

        Args:
            mes_aniversario: (obrigatorio)

        Return:
            list: lista de tuples com registros filtrados pelo mes
        '''
        lis = list()
        mes_aniversario = '{:02d}'.format(int(mes_aniversario))

        for item in self.lista:
            if mes_aniversario in item[3].split('-')[1]:
                lis.append(item)
        
        return lis
 

    def relatorio_lista_para_txt(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            for registro in lista:
                f.write(40 * '*' + '\n')
                for i in range(len(registro)):
                    f.write(registro[i])
                    f.write('\n')
 

    def relatorio_lista_para_cvs(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            writer = csv.writer(f)
            for registro in lista:
                writer.writerow(registro)
 

if __name__ == "__main__":
    objeto = Sprint2()
    objeto.carregar_arquivo_para_lista('arquivo_1.csv')
    objeto.carregar_arquivo_para_lista('arquivo_2.csv')
    objeto.carregar_arquivo_para_lista('arquivo_3.csv')
    
    # Descomentar para testar 
    # Relatório de pessoas com sobrenome 'Silva'
    lista = objeto.busca_trecho_nome('Silva')
    objeto.relatorio_lista_para_txt('relatorio_1.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_1.csv', lista)
    # Relatório de tentativas de fraude com vencimento de cartão em dezembro
    lista = objeto.busca_mes_vencimento_cartao_credito('12')
    objeto.relatorio_lista_para_txt('relatorio_2.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_2.csv', lista)