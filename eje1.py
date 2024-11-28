# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE DETERMINA EL PRECIO DE VENTA POR CADA KG DE HUEVO ***")

# PROMPTING THE USER
Gallinas = int(print("Cuántas gallinas hay en la granja: "))

i=0
Promedio = 0

while i < Gallinas:
  i += 1

  Peso = float(print("Ingresar el peso de la gallina:"))
  Altura = float(print("Ingresar la altura de la gallina:"))
  Huevos = int(print("Ingresar el número de huevos que pone la gallina:"))
  
  Calidad = (Peso * Altura) / Huevos
