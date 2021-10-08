from banco.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de pessoa Juridica.
    Limite padrão da conta: R$ 1500,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe ContaPessoaJuridica.
        Extrai do dicionário kwargs:
        - Nome
        - CNPJ
        - Limite
        - Saldo
        """
        self.extrato = []
        self.cnpj = kwargs.get('cnpj', None)
        if self.cnpj == None:
            raise ValueError('CNPJ inválido')
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 1500)

    
    def saque(self, valor):
        error_msg = 'Valor do saque supera seu saldo e seu limite'
        return super().saque(valor, error_msg)


    def deposito(self, valor):
        super().deposito(valor)


    def get_extrato(self):
        return super().get_extrato()


    def __str__(self):
        return f'Conta PJ:{self.nome},saldo={self.saldo}'

    
    def __repr__(self):
        return f'Conta PJ:{self.nome},saldo={self.saldo}'