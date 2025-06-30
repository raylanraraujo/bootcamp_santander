class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo # definindo como uma variável privada
        self.numero_agencia = numero_agencia #definido como uma variavel publica 

    def depositar(self, valor):
        # ... aque é apenas fingindo que tem o código de verificaçao das regras 
        self._saldo += valor

    def sacar(self, valor):
        # ... aque é apenas fingindo que tem o código de verificaçao das regras 
        self._saldo -= valor

    def mostar_saldo(self):
        return self._saldo
conta = Conta("0001", 100)#instanciar uma conta e definir o saldo dela inicial de 100
# conta._saldo += 100 # e muito menos fazer a atualização da variável definida como privada, mesmo que o c;odigo venha a funcionar. 
conta.depositar(100)# o correto e chamar o metodo de deposito e adicionar o valor a conta 
print(conta._saldo) # exibe o valor do meu saldo sem nenhum tipo de segurança. Apesar de ser possível acessar o valor do saldo, isso é errado. Pois pela convenção o programado que escreveu o código definiu explicitamente que você não deveria fazer esse acesso. Isso que está sendo feito é driblar o encapsulamento.

#Por ser uma variavel privada, eu só consigo acessá-la dentro do meu escopo da minha classe.

print(conta.mostar_saldo())