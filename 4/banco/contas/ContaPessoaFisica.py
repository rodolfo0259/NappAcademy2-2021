from banco.contas.Conta import Conta


class ContaPessoaFisica(Conta):
    """
    Classe representa a conta corrente de pessoa física.
    Limite padrão da conta: R$ 500,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe PessoaFísica.
        Extrai do dicionário kwargs:
        - Nome
        - CPF
        - Limite
        - Saldo
        """
        self.cpf = kwargs.get('cpf', None)
        if self.cpf == None:
            raise ValueError('CPF inválido')
        super(ContaPessoaFisica, self).__init__(**kwargs)


    def saque(self, valor):
        error_msg = 'Valor do saque supera seu saldo e seu limite'
        return super().saque(valor, error_msg)


    def deposito(self, valor):
        super().deposito(valor)


    def get_extrato(self):
        return super().get_extrato()


    def __str__(self):
        return "Conta PF:" + self.nome + ",saldo=" + str(self.saldo)

    def __repr__(self):
        return  "Conta PF:" + self.nome + ",saldo=" + str(self.saldo)