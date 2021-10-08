class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe via kwargs :
        - nome
        - limite
        - saldo

        Raises:
            ValueError: Nome Informado seja vazio.
            ValueError: Saldo seja menor que zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        if self.nome == None:
            raise ValueError('Nome não informado')
        self.saldo = 0
        saldo = kwargs.get('saldo', self.saldo)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))


    def saque(self, valor, error_msg: str='Valor do saque supera seu saldo e seu limite'):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque
            error_msg (str): 
                Recebe mensagem de erro especifica/customizada
                de cada conta caso exista, senão será usado a 
                frase padrão para exibir caso ocorra 
                algo de errado

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError(error_msg)
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')


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
            return valor
        raise TypeError('O depósito precisa ser numérico')


    def get_extrato(self)->list:
        """
        Retorna a lista dos saques e depósitos feitos na conta.

        Returns:
            List: Lista de operações
        """
        return self.extrato