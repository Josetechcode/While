# DISPLAY TITLE
print("*** PROGRAMA QUE DETERMINA CUANTOS VEHÍCULOS DE CADA COLOR DE CALCOMANÍA INGRESAN A LA CIUDAD ***")

# COUNTERS AS PER STICKER COLOUR
Ama = 0
Ros = 0
Roj = 0
Ver = 0
Azu = 0
Dig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Num = int ( input ("Cuántos vehículos desea contar: "))

i = 0
while i < Num:
  i += 1

  Dig = int ( input ("Ingrese el último dígito de la placa de tránsito: "))

  if Dig not in Dig_list:
    print ("Ingresar un valor válido (0 a 9): ")
  elif Dig == 1 or Dig == 2:
    Ama += 1
  elif Dig == 3 or Dig == 4:
    Ros += 1
  elif Dig == 5 or Dig == 6:
    Roj += 1
  elif Dig == 7 or Dig == 8:
    Ver += 1
  elif Dig == 9 or Dig == 0:
    Azu += 1

print (f"a) Cantidad de vehículo de calcomanía amarilla:{Ama}\nb) Cantidad de vehículo de calcomanía rosa: {Ros}\nc) Cantidad de vehículo de calcomanía roja: {Roj}\nd) Cantidad de vehículo de calcomanía verde: {Ver}\ne) Cantidad de vehículo de calcomanía azul: {Azu}")