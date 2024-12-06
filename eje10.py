# DISPLAY TITLE
print("*** PROGRAMA QUE REALIZA UN ESTUDIO DEL TRÁFICO TOMANDO UNA MUESTRA DE 'n' VEHÍCULOS")

Tur = 0 # TURISMO VEHICLE COUNTER
Aut = 0 # AUTOBUS VEHICLE COUNTER
Cam = 0 # CAMION VEHICLE COUNTER
Mot = 0 # MOTOCICLETA VEHICLE COUNTER
Passengers = 0

Vehiculos = int(input("Definir tamaño de la muestra (número de vehículos): "))

print(f"Se va a dar inicio al estudio. De acuerdo a lo anterior, se va a tomar una muestra de {Vehiculos} vehiculo(s).")

i = 0
while i < Vehiculos:
  i += 1
  
  Tipo = int(input("Ingresar el tipo de vehículo (1, 2, 3, 4):\n1. Turismo.\n2. Autobus.\n3. Camión.\n4. Motocicleta.\n"))

  if Tipo == 1:
    Tur = Tur + 1 
    print(f"Has ingresado exitosamente la entrada número {i} y quedan pendientes ",Vehiculos-i,"entrada(s) (vehículo tipo turismo)")
    Passengers1 = int(input("Ingresar cantidad de ocupantes: "))
    Passengers += Passengers1 
  elif Tipo == 2:
    Aut = Aut + 1
    print(f"Has ingresado exitosamente la entrada número {i} y quedan pendientes ",Vehiculos-i,"entrada(s) (Vehículo tipo autobus).")
  elif Tipo == 3:
    Cam = Cam + 1
    print(f"Has ingresado exitosamente la entrada número {i} y quedan pendientes ",Vehiculos-i,"entrada(s) (Vehículo tipo camión).")
  elif Tipo == 4:
    Mot = Mot + 1 
    print(f"Has ingresado exitosamente la entrada número {i} y quedan pendientes ",Vehiculos-i,"entrada(s) (Vehículo tipo motocicleta).")

Total = Tur + Cam + Aut + Mot

print("Cantidad de vehículos tipo turismo: ",Tur,"Correspondiete al",(Tur/Total)*100," porciento de la muestra\nCantidad de vehículos tipo camión: ",Cam,"Correspondiete al",(Cam/Total)*100,"porciento de la muestra\nCantidad de vehículos tipo automovil: ",Aut,"Correspondiete al",(Aut/Total)*100,"porciento de la muestra\nCantidad de vehículos tipo motocicleta: ",Mot,"Correspondiete al",(Mot/Total)*100,"porciento de la muestra\nCantidad de turistas: ",Passengers,)