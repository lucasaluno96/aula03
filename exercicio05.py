#receba 3 notas e veja se foi aprovado ou nao com nota de aprovação 7

nota1 = float (input("sua primeira nota: "))
nota2 = float (input("sua segunda nota: "))
nota3 = float (input("sua terceira nota: "))
media = (nota1 + nota2 + nota3) /3
if media >= 7:
    print(f"parabens voce passou com nota media {media}")
else:
    if media<4:
        print(f"reprovado")
    else:
        print(f"recuperação")

teste