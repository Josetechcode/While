# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE DETERMINA LA DISTANCIA A CADA SEGUNDO QUE SEPARA UN AVIÓN DE UN PROYECTIL ***")

# DECLARING AND INITIALIZING THE VARIABLES 
Distancia = 0
Velocidad = 800000 / 3600
Aceleracion = 0.02
Tiempo = 0

while Distancia <= 10000: # RUNNING THE LOOP UP TO 10.OOO m OR MORE
    
    Tiempo += 1

    Distancia = Velocidad * Tiempo + 1/2 * Aceleracion * Tiempo**2 + Distancia

    # DISPLAYING THE RESULT
    print (f"Cuando ha pasado {Tiempo} segundo(s) la distancia es: {Distancia} metros.")