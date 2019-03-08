cont=0
a=int(input('Ingrese un número'))
for i in range (1,a+1):
  if a%i==0:
    cont=cont+1
if cont>2:
  print('El numero es primo')
else:
  print('El número no es primo')