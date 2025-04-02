nome = input("digite aqui seu nome: ")
idade = int(input("digite sua idade: "))
salario = float(input("qual o seu salario? "))

#aumento de salario
aumento = int(input("digite aqui % de aumento"))
novosalario = salario*aumento/100 + salario

print(f"nome:{nome}\n idade:{idade}\n salario:{salario}\n aumento%:{aumento}\n novo salario:{novosalario:.2f}")