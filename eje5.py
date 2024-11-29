# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE DETERMINA QUÉ CANTIDAD DE ALUMNOS NO TIENEN DERECHO A NIVELACIÓN (nota promedio mayor 2.5) ***")

# ⚠ ⚠ ⚠ ⚠ ⚠ EL CASO NO DA LOS CRITERIOS PARA DEFINIR QUÉ ALUMNOS TIENEN DERECHO AL EXAMEN DE NIVELACION
# ⚠ ⚠ ⚠ ⚠ ⚠ EL CRITERIO ESTABLECIDO SERÁ NOTA SUPERIOR A 2.5 (0 - 5)

i = 0 # INITIALIZING VARIABLE TO COUNT STUDENTS
k = 0 # INITIALIZING VARIABLE TO COUNT STUDENTS WHO DESERVE AN ADDITIONAL ASSESMENT
l = 0 # INITIALIZING VARIABLE TO COUNT STUDENTS WHO DOES NOT DESERVE AN ADDITIONAL ASSESMENT

while i < 40: # THE LOOP WILL RUN UP TO 40 TIMES (STUDENTS)
    i += 1 # STUDENTS COUNTER
    print(f"A continuación vamos a solicitar las 5 notas del estudiante número {i} (0 - 5).")

    j = 0 # INITIALIZING VARIABLE TO COUNT NOTES
    nota = 0
    Suma = 0
    
    while j < 5: # THE LOOP WILL RUN UP TO 5 TIMES (NOTES)
        j += 1 # NOTES COUNTER
        nota = float(input("Ingrese la nota y presione 'enter' para ingresar la siguiente nota (0 - 5): "))
        Suma = Suma + nota
    
    Promedio = Suma / 5

    if Promedio > 2.5:
        k += 1 # STUDENTS WHO DESERVE AN ADDITIONAL ASSESMENT COUNTER
        print(f"El estudiante número {i} obtuvo una nota promedio de {Promedio}, por lo tanto, tiene derecho a presentar exámen de nivelación.")
    else:
        l += 1 # STUDENTS WHO DOES NOT DESERVE AN ADDITIONAL ASSESMENT COUNTER
        print(f"El estudiante número {i} obtuvo una nota promedio de {Promedio}, por lo tanto, no tiene derecho a presentar exámen de nivelación.")

print(f"Cantidad de estudiantes que tienen derecho a examen de nivelacion (promedio mayor a 2.5): {k}\nCantidad de estudiantes que no tienen derecho a examen de nivelacion (promedio menor o igual a 2.5): {l}")
print("¡El programa ha finalizado!")