from classes.Pessoa import*

p1 = Pessoa("João",65,23)
p2 = Pessoa("Maria",55,20)

print(f'O nome é {p1.nome} e pesa {p1.peso}')
p1.comer("coxinha","Coca-zero")
p1.falar("olá mundo")
p2.dormir()