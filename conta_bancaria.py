class Conta_bancaria:
    '''
    Conta bancaria para fazer saques e depositos
    '''
    def __init__(self ,id , nome , saldo):
        self.identificacao = id
        self.usuario = nome
        self.valor = saldo

    def depositar(self , quantia):
        '''
        Se o deposito em conta for maior que o esperado : False
        se não : True
        '''
        if quantia < 0:
            print('Deposito negado')
        else:
            self.valor += quantia
            print(f'Valor {quantia} caiu na conta ID:{self.identificacao}')


    #função de sacar o valor disponivel dentro da conta
    def sacar(self, quantia):
        '''
        Se o valor que sera sacado foi maior que o na conta , não autoriza
        Se o valor sacado estiver dentro do valor : True
        '''
        if quantia > self.valor:
            print(f'Ação não autorizada , valor imcopativel')
        else:
            self.valor -= quantia
            print(f'Valor {quantia} sacado na conta ID:{self.identificacao}')


    def __str__(self):
        return f"O usuario {self.usuario} ID {self.identificacao} teve o valor {self.valor}"
    
    

conta1 = Conta_bancaria(425064 , 'Adriel' , 2800)
conta1.depositar(20)
conta1.sacar(4)

print(conta1)
