
"""Ejercicio 3"""
def factorial(n):	
	x = 1
	if(n>0):
		x=factorial(n-1)
		x=x*n
	else:
		x=1
	return x

def ecuacion(n):
	contador = 0
	for i in range(1,n+1):
		f = factorial(i);
		contador= contador + (1/f)
		pass
	return contador	

def run():
	print("1/1!+1/2!+1/3!...1/n!")
	numero = int(input("inserta el numero n:"))
	calculo=ecuacion(numero)
	print ("El resultado de la ecuacion de %s es %s" %(numero,calculo))

if __name__=='__main__':
	run()