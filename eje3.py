# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE CALCULA LA NOTA PROMEDIO DE 5 ESTUDIANTES ***")

i = 0
Base_Datos = []
Promedio = 0

while i < 5:
  i += 1
  Nombre = input("Ingrese el(los) nombre(s) y apellido(s) del estudiante: ")
  Edad = input("Ingrese la edad del estudiante: ").capitalize()
  Nota = float(input("Ingrese la nota del estudiante: "))

  Base_Datos.append(Nombre)
  Base_Datos.append(Edad)
  Base_Datos.append(Nota)

  Promedio = Nota + Promedio

print(f"Los datos ingresados son los siguientes [Nombre Completo, Edad, Nota]:\n{Base_Datos}\nEl programa ha terminado.\nLa nota promedio es: {Promedio/5}.")