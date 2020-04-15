def prestamo():
	A = int(input("Ingrese el valor del prestamo:"))
	N = int(input("A cuanos años: "))
	I = int(input("Tasa de interes: "))
	Z = A*(I + 1 )**N
	return "El valor total a pagar es de %s" %Z

print(prestamo())
input("-----oprima ara salir------"))