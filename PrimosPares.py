
"""Ejercicio 4"""
def primos():
	contador = 0
	for i in range(1,(100+1)):
		comprobante = 0
		for j in range(1,(i+1)):
			if (i % j) == 0:
				comprobante = comprobante + 1
		if comprobante == 2:
			contador = contador+i
			print ("%s es primo" % i)
	return "la suma de numeros primos entre 0 y 100 es de %s" %contador

def pares():
	contador = 0
	sumatoria = 0
	for i in range(1,10+1):	
		if (i%2) == 0:
			contador = contador+1
			sumatoria = sumatoria + i
	return "la promedio de numeros pares entre 0 y 100 es de %s" %(sumatoria/contador)	
		

print (primos())
print(pares())



