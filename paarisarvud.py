numbrid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

paariskogus = 0
paarituKogus = 0

for number in numbrid:
    if number % 2 == 0:
        paariskogus += 1
    else:
        paarituKogus += 1

print("Paarisarve kogus: ", paariskogus)
print("Paaritute arv: ", paarituKogus)