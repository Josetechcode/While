# DISPLAY TITLE
print("*** PROGRAMA QUE REALIZA UN ESTUDIO DEL TRÁFICO TOMANDO UNA MUESTRA DE 'n' VEHÍCULOS")

Tur = 0 # TURISMO VEHICLE COUNTER
Aut = 0 # AUTOBUS VEHICLE COUNTER
Cam = 0 # CAMION VEHICLE COUNTER
Mot = 0 # MOTOCICLETA VEHICLE COUNTER
Passengers = 0

Vehiculos = int(input("Definir tamaño de la muestra (número de vehículos): "))

print(f"Se va a dar inicio al estudio. De acuerdo a lo anterios, se va a tomar una muestra de {Vehiculos} vehiculo(s).")

i = 0
while i < Vehiculos:
  i += 1
  
  Tipo = int(input("Ingresar el tipo de vehículo (1, 2,3, 4):\n1. Turismo.\n2. Autobus.\n3. Camión.\n4. Motoicleta.\n"))

  if Tipo == 1:
    Tur += Tur 
    Passengers = input("Has ingresado exitosamente la entrada número {i} y quedan pendientes ",i-10,"entradas". (vehículo tipo turismo). Ingresar cantidad de ocupantes: ")
    Passengers += Passengers
  elif Tipo == 2:
    Aut += Aut
    print("Has ingresado exitosamente la entrada número {i} y quedan pendientes ",i-10,"entradas".  Vehículo tipo autobus.")
  elif Tipo == 3:
    Cam += Cam
    print("Has ingresado exitosamente la entrada número {i} y quedan pendientes ",i-10,"entradas". Vehículo tipo camión.")
  elif Tipo == 4:
    Mot += Mot 
    print("Has ingresado exitosamente la entrada número {i} y quedan pendientes ",i-10,"entradas". Vehículo tipo motocicleta.")

print(Tur, Cam, Aut, Mot,"Cantidad de turistas: ",Passengers)