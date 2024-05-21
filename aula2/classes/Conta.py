class Conta():
    def __init__(self, nomeCliente, numero, tipo):
        self.nomeCliente = nomeCliente
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0.00
        self.status = False
    
    def depositar(self, valor):
       if(self.status == True):
           self.saldo = self.saldo + valor
           print(f"Deposito no valor de R$ {valor} realizado com sucesso")
       else:
           print("Conta está desativada não foi possível realizar esta ação")

    def sacar(self,valor):
         if(self.status == True):
             if(self.saldo >= valor):
               self.saldo = self.saldo - valor
               print(f"Saque no valor de R$ {valor} realizado com sucesso")
             else:
                print("saldo insuficiente!")
         else:
             print("Conta está desativada não foi possível realizar esta ação")          
    def verificarsaldo(self):
         if(self.status == True):
           print(f"Saldo : R$ {self.saldo}")
         else:
           print("Conta está desativada não foi possível realizar esta ação")
  
    def ativar(self):
        if(self.status == True):
           print("Conta já está ativada")
        else:
           if (saldo == 0):
            self.status = True
            print("Conta ativada com sucesso") 
           else:
            print("Conta ainda possui saldo não pode ser desativada")
    def desativar(self): 
         if(self.status == False):
           print("Conta já está desativada")
         else:
           self.status = False
           print("Conta desativada com sucesso") 

   