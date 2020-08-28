pasos = 1
lista = int(input("tamaño de la lista: "))
numero= int(input("escriba un numero: "))
num = 0;
num2 = lista;
contador = 0
while(contador == 0):
  print("------------------ van ", pasos , " pasos -------------------")
  num2 = int((num2+1)/2)
  varAdivino = num2 + num

  print("1. es menor que ", varAdivino)
  print("2. es mayor que ", varAdivino)
  print("3. es su numero ", varAdivino)
  nom= int(input("----Elije: "))

  if(nom==1):
    num = varAdivino - num2
    
  if(nom==2):
    num = varAdivino

  if(nom==3):
    contador=1
    if(varAdivino == numero):
      print("---------- El numero es: ", varAdivino , "se adivino en ", pasos , "pasos -------------")
    else:
      print("equivocado")
      contador=0
  pasos = pasos + 1