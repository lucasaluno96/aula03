#receba 2 time, receba quantos gols cada um fez e diga qual foi o vencendor ou empate

#time
t1 = input("time 1? ")
gt1 = int(input("quantos gols do time 1? "))
t2 = input("time 2? ")
gt2 = int(input("quantos gols do time 2? "))

if gt1 == gt2 :
    print("Empate")
else:
    if gt1 > gt2 :
        print(f"O time {t1} é o vencedor")
    else:
        if gt2 > gt1 :
            print(f" O time {t2} é o vencedor")


