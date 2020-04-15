
"""Ejercicio 1"""
from random import randrange
import math

class Triangulo(object):
	def __init__(self):
		self.ladoA = randrange(5,10)
		self.ladoB = randrange(5,10)
		self.ladoC = randrange(5,10)
		self.a = math.degrees(math.acos((self.ladoB**2 + self.ladoC**2 - self.ladoA**2) / (2* self.ladoB * self.ladoC) ))
		self.b = math.degrees(math.acos((self.ladoA**2 + self.ladoC**2 - self.ladoB**2) / (2* self.ladoA * self.ladoC) ))
		self.c = 180 - self.a - self.b

tring = []

for i in range(15):
	tringlo = Triangulo()
	tring.append(tringlo)
	pass

print()

for i in range(15):
	if tring[i].a == 90 or tring[i].b == 90 or tring[i].c == 90:
		print("el triagulo %i es Rectangulo"  % i+1)
		pass
	elif tring[i].a < 90 and tring[i].b < 90 and tring[i].c < 90:
		print("el triagulo %s es acutángulo"  %(i+1))
		pass
	elif tring[i].a > 90 or tring[i].b > 90 or tring[i].c > 90:
		print("el triagulo %s es obtusángulo"  %(i+1))
		pass
	pass



