# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE DETERMINA CUANTAS MUJERES HABÍA EN UN BAILE, DONDE LA PRIMERA DAMA BAILÓ CON 7 Y LA SIGUIENTE VA BAILANDO CON 1 MÁS ***")

i = 0 # INITIALIZE VARIABLE TO COUNT WOMEN
j = 6 # INITIALIZE VARIABLE TO COUNT MEN

while j < 42:

    i += 1 # WOMEN COUNTER
    j += 1  # MEN COUNTER
    
    # DISPLAY COUNTERS STATUS
    print(F"La mujer número {i} bailó con {j} hombres.")

print(f"Los asistentes a la fiesta son:\na. Hombres: {j}.\nb. Mujeres: {i}.\n¡El programa ha terminado!")