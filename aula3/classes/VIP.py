from classes.Ingresso import*
class Vip(Ingresso):
    def __init__(self, valor):
     super().__init__(valor)

    def imprimirValor(self):
      self.valor  = self.valor*1.5
      return super().imprimirValor()
