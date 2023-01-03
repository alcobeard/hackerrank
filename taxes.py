x = int(input())

tax = 0

if x < 42708:
    if x < 15528:
        tax = 0
    else:
        tax = 15
else:
    if x < 132407:
        tax = 25
    else:
        tax = 28

calculated_tax = x * (tax / 100)

if calculated_tax % 2 != 0:
    calculated_tax += 1

print(f'The tax for {x} is {tax}%. That is {int(calculated_tax)} dollars!')