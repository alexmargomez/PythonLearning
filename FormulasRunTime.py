import math
import time


def init():
  cont = 0
  while(cont==0):
    print ("--Tiempo de Ejecucion en milisegundos--")
    print ("   1. Bynary Search (Log2 n)")
    print ("   2. Simple Search (n)")
    print ("   3. quicksort (n* log2 n)")
    print ("   4. selection Sort (n^2)")
    print ("   otra tecla para salir")
    valor = int(input("...Elije una opcion: "))
    cont = opciones(valor)
    time.sleep(1)
    print("..................................................................")

def opciones(v):
  if(v==1):
    cant = float(input("Digite el valor : "))
    resl = math.log2(cant)  
    print("El tiempo es de:",resl ," milisegundos")
    return 0
  if(v==2):
    cant = float(input("Digite el valor : "))
    resl = cant  
    print("El tiempo es de:",resl ," milisegundos")
    return 0
  if(v==3):
    cant = float(input("Digite el valor : "))
    resl = cant *(math.log2(cant)) 
    print("El tiempo es de:",resl ," milisegundos")
    return 0
  if(v==4):
    cant = float(input("Digite el valor : "))
    resl = cant*cant 
    print("El tiempo es de:",resl ," milisegundos")
    return 0
  if(v!= 1,2,3,4):
    print ("bye...")
    return 1
  
  
init()
