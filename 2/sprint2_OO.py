import csv

class Sprint2:
    def __init__(self):
        pass
        
    def carregar_arquivo_para_lista(self, nome_arquivo):
        pass

    def busca_trecho_nome(self, nome):
        pass

    def busca_email(self, email):
        pass

    def busca_estado(self):
        pass
 
    def busca_mes_vencimento_cartao_credito(self, mes_vencimento):
        pass

    def busca_prefixo_sufixo_ip(self, prefixo_ip='192', sufixo_ip='0'):
        pass

    def contar_ocorrencia_por_dominio_hostname(self, *dominios):
        pass
 
    def contar_ocorrencia_por_dominio_email(self, *dominios):
        pass
 
    def busca_mes_aniversario(self, mes_aniversario):
        pass
 
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
    
    """
    # Descomentar para testar 
    # Relatório de pessoas com sobrenome 'Silva'
    lista = objeto.busca_trecho_nome('Silva')
    objeto.relatorio_lista_para_txt('relatorio_1.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_1.csv', lista)
    # Relatório de tentativas de fraude com vencimento de cartão em dezembro
    lista = objeto.busca_mes_vencimento_cartao_credito('12')
    objeto.relatorio_lista_para_txt('relatorio_2.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_2.csv', lista)
    """