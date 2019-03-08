contador=0
i=1
a=int(input("ingrese el numero"))
while i<=a:
  i=i+1
  if a%i==0:
    contador=contador+1
if contador>2:
  print("el numero no es primo")
else:
 print("el numero es primo")