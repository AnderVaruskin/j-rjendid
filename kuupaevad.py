from datetime import datetime

while True:
    try:
        kuupaev_str = input("Sisestage kuupäev vormingus DD.MM.YYYY: ")
        kuupaev = datetime.strptime(kuupaev_str, '%d.%m.%Y')
        break
    except ValueError:
        print("Vigane kuupäeva vorming. Palun sisestage kuupäev vormingus DD.MM.YYYY.")

päev = kuupaev.day
kuu_nimi = kuupaev.strftime("%B")
aasta = kuupaev.year

print(f"{päev}. {kuu_nimi} {aasta}")