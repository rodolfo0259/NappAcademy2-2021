from banco.contas.Conta import Conta

class ContaPoupanca(Conta):
   def __init__(self,  **kwargs):
      """
      Construtor da classe ContaPoupanca.
      Extrai do dicionário kwargs:
      - Nome
      - CPF
      - Saldo
      """
      self.extrato = []
      self.cpf = kwargs.get('cpf', None)
      self.nome = kwargs.get('nome', None)
      self.saldo = kwargs.get('saldo', None)
      if self.cpf == None:
         raise ValueError('CPF inválido')
      super(ContaPoupanca, self).__init__(**kwargs)
      self.limite = kwargs.get('limite', 0)
      self.error_msg = 'Valor do saque supera seu saldo.'


   def rendimento_aniversario(self, juros: float)-> None:
      """
      Ira calcular o rendimento do juros(porcentagem)
      sobre o valor em conta(saldo)
      Args:
         juros: porcentagem de juros, 0 => x <= 1
      """
      if juros >= 0 and juros <=1:
         self.saldo += self.saldo * juros
      else:
         raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')


   def __str__(self):
      return f'Conta Poupança:{self.nome}, saldo={self.saldo}'

   def __repr__(self):
      return f'Conta Poupança:{self.nome}, saldo={self.saldo}'
