valor = 222
cem = 0
cinq = 0
vint = 0
dez = 0
cinco = 0
um = 0

while valor >= 1:
    if valor >= 100:
        valor = valor - 100
        cem += 1
    elif valor >= 50:
        valor = valor - 50
        cinq += 1
    elif valor >= 20:
        valor = valor - 20
        vint += 1
    elif valor >= 10:
        valor = valor - 10
        dez += 1
    elif valor >= 5:
        valor = valor - 5
        cinco += 1
    else:
        valor = valor - 1
        um += 1

print("Notas de R$ 100:", cem)
print("Notas de R$ 50:", cinq)
print("Notas de R$ 20:", vint)
print("Notas de R$ 10:", dez)
print("Notas de R$ 5:", cinco)
print("Notas de R$ 1:", um)
