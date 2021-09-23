import sqlite3


class DAO:
    def __init__(self, nome_banco_dados):
        self._nome_banco_dados = nome_banco_dados
        self.conn = sqlite3.connect(self._nome_banco_dados)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM vendas;")


    def get_registros_todos(self)->list:
        '''
        Traz todos os registros do banco
        Return:
            lista com tuples de todos os registros
        '''
        lis = []
        sql = "SELECT * FROM vendas;"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lis.append(registro)
        return lis


    def get_registros_por_produto(self, produto:str)-> list:
        '''
        Traz todos os registros de um produto
        Args:
            produto: produto a ser encontrado
        Return:
            lista com tuples de todos os registros com determinado produto
        '''
        lis = []
        sql = f"SELECT * FROM vendas WHERE produto = '{produto}'"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lis.append(registro)
        return lis


    def get_registros_por_data(self, data):
        lista = []
        sql = "SELECT * FROM vendas where criado_em = '" + data + "';"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista


    def get_registros_quantidade(self, minimo:int=0, maximo:int=20)->list:
        '''
        Traz todos registros onde a quantidade esteja entre o minimo e maximo
        Args:
            minimo: quantidade minima em estoque
            maximo: quantidade maxima em estoque
        Return:
            Uma lista de tuples(registros) encontrados
        '''
        lista = []
        sql = "SELECT * FROM vendas where quantidade  > " + str(minimo)
        sql = sql + " AND quantidade < " + str(maximo) + ";"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista


    def get_registros_preco(self, minimo=30, maximo=40)->list:
        '''
        Traz todos os registros em um range de precos
        Args:
            minimo: valor minimo
            maximo: valor maximo
        Return:
            lista com tuples de todos os registros dentro do range de precos
        '''
        lis = []
        sql = f"SELECT * FROM vendas WHERE preco > '{minimo}' and preco < {maximo}"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lis.append(registro)
        return lis


    def close(self):
        self.conn.close()


    def __str__(self):
        return self._nome_banco_dados


    def __repr__(self):
        return 'DAO: ' + self._nome_banco_dados
