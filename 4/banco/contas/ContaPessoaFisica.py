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

    def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def get_extrato(self):
        """
        Retorna a lista dos saques e depósitos feitos na conta.

        Returns:
            List: Lista de operações
        """
        return self.extrato

    def __str__(self):
        return "Conta PF:" + self.nome + ",saldo=" + str(self.saldo)

    def __repr__(self):
        return  "Conta PF:" + self.nome + ",saldo=" + str(self.saldo)