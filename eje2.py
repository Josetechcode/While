# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE CALCULA LAS OPERACIONES BÁSICAS ENTRE DOS NÚMEROS HASTA 10 VECES ***")

i = 0

# INITIALIZING THE LOOP TO RUN 10 LOOPS
loops = 10
while i < loops:
  i += 1

  # PROMTING THE USER 
  Num1 = float (input("INGRESAR EL PRIMER NÚMERO: "))

  Num2 = float (input("INGRESAR EL PRIMER NÚMERO: "))

  print("los resultados son los siguientes:\na. Suma = ",Num1 + Num2,"\nb. Resta = ", Num1 - Num2,"\nc. Multiplicación = ",Num1*Num2,"\nd. División = ",Num1 / Num2)

print ("¡Se han completado 10 procesos!")