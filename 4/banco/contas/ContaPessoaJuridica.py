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


    def deposito(self, saldo_deposito):
        """
        Processa o saldo depositado para a Conta e adiciona ao extrato

        Args:
            Valor a ser depositado: int ou float
        
        Raises:
            TypeError:  Valor precisa ser numerico
            ValueError: Valor negativo
        """
        if type(saldo_deposito) == float or type(saldo_deposito) == int:
            pass
        else:
            raise TypeError('O depósito precisa ser numérico')

        if saldo_deposito <= 0:
            raise ValueError('Valor do depósito precisa ser maior que zero')
        
        self.saldo += saldo_deposito
        self.extrato.append(('D', saldo_deposito))

    
    def saque(self, saldo_saque):
        """
        Processa o saldo retirado(saque) da Conta e adiciona ao extrato

        Args:
            Valor a ser saquado: int ou float
        
        Raises:
            TypeError:  Valor precisa ser numerico
            ValueError: Valor acima do limite
        """
        if type(saldo_saque) == float or type(saldo_saque) == int:
            pass
        else:
            raise TypeError('O valor do saque precisa ser numérico')

        if saldo_saque > (self.saldo+self.limite):
            raise ValueError('Valor do saque supera seu saldo e seu limite')

        self.saldo -= saldo_saque
        self.extrato.append(('S', saldo_saque))
        return saldo_saque


    def get_extrato(self)->list:
        """
        Retorna a lista dos extratos da conta
        """
        return self.extrato



    def __str__(self):
        return f'Conta PJ:{self.nome},saldo={self.saldo}'

    
    def __repr__(self):
        return f'Conta PJ:{self.nome},saldo={self.saldo}'