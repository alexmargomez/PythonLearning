
TI = int(input("Tiempo de la llamada en minutos:"))
DI = str(input("Tipo de dia:"))
TU = str(input("Turno ´matutino´ o ´vesparino´"))

pag = 0
imp = 0

for i in range(TI):
    if i <= 5:
        pag =pag + 1
    elif i <= 8:
        pag = pag + 80
    elif i <= 10:
        pag = pag + 70
    elif i > 10:
        pag = pag + 50
    i = i + 1

print(pag)

if DI == "domingo":
    imp = pag*0.03
else:
    if TU == "matutino":
        imp = pag * 0.15
    elif TU == "vesperino":
        imp = pag * 0.10

print("el pago a realizar es $%s" % (pag + imp))
