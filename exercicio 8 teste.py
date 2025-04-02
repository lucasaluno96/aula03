#receba 3 notas e veja se foi aprovado ou nao com nota de aprovação 7
from selectors import SelectSelector

n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
n3 = float(input("terceira nota: "))

media = (n1 + n2 + n3) /3
if media >= 7 :
    print(f"parabens voce foi aprovado com nota {media:.2f}")
else:
    if media < 4 :
        print(f"infelizmente voce foi reprovado com nota {media:.2f}")
    else:
        print(f"recuperação")