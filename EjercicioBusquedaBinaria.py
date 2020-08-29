pasos = 1
lista = int(input("tamaño de la lista: "))
numero= int(input("escriba un numero: "))
num = 0;
num2 = lista;
contador = 0
while(contador == 0):
  
  num2 = int((num2+1)/2)
  varAdivino = num2 + num

  if(varAdivino == numero):
      print("---------- El numero es: ", varAdivino , "se adivino en ", (pasos - 1) , "pasos -------------")
      contador=1
  else:
    print("------------------ van ", pasos , " pasos -------------------")
    print("1. es menor que ", varAdivino)
    print("2. es mayor que ", varAdivino)

    nom= int(input("----Elije: "))

    if(nom==1):
      num = varAdivino - num2
      
    if(nom==2):
      num = varAdivino

  pasos = pasos + 1