"""Ejercicio 2"""
def factorial(n):	
	x = 1
	if(n>0):
		x=factorial(n-1)
		x=x*n
	else:
		x=1
	return x

def run():
	numero = int(input("inserta un numero "))
	calculo=factorial(numero)
	print("El factorial de %s es %s" %(numero,calculo))


if __name__ == '__main__':
	run()




