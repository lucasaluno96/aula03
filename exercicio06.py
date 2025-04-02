time1 = input("primeiro time")
time2 = input("segundo time")
goldotime1 = int(input("quantos gols do time 1?: "))
goldotime2 = int(input("quantos gols do time 2?: "))

print(f"{time1} {goldotime1} x {time2} {goldotime2}")

if goldotime1 > goldotime2 :
    print(f" vencedor {time1}")
else:
    if goldotime1 < goldotime2 :
        print(f"vencedor {time2}")
    else:
        print(f"empate")
teste