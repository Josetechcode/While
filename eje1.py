# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE DETERMINA EL PRECIO DE VENTA POR CADA KG DE HUEVO ***")

# PROMPTING THE USER AND INITIALIZING VARIABLES
Gallinas = int(input("Cuántas gallinas hay en la granja: "))

# INITIALIZING AND DECLARING VARIABLES
i=0
Calidad = 0

# RUNNING THE LOOP AND SAVING INFO
while i < Gallinas:
  i += 1

  # PROMTING THE USER
  Peso = float(input("Ingresar el peso de la gallina:"))
  Altura = float(input("Ingresar la altura de la gallina:"))
  Huevos = int(input("Ingresar el número de huevos que pone la gallina:"))

  # CALCULATING THE CHICKEN QUALITY  
  Calidad = Calidad + (Peso * Altura) / Huevos

Precio = Calidad / Gallinas

print (f"El precio de venta por cada kg de huevo es: {Precio}.")