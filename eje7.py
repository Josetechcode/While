# DISPLAYING THE PROGRAM TITLE
print("*** PROGRAMA QUE CALCULA SALARIO DE VENDEDORES ***")

# ⚠ ⚠ ⚠ ⚠ ⚠ EL CASO DE ESTUDIO NO DEFINE EL SALARIO BASE

# DECLARING AND INITIALING VARIABLES

Venderores = int(input("Cuantos vendedores va a ingresar: "))

i = 0 # SELLER COUNTER
while i < Venderores:
    i += 1
    print(f"A continuación ingrese las 3 ventas correspondientes al vendedor número {i}. Una vez ingrese el valor de una venta, presione 'enter' para ingresar la siguiente ventas hasta completar 3 ventas.")

    j = 0
    Total_Venta = 0
    while j < 3:
        j += 1
        Valor_Venta = float (input("Ingrese el valor de la venta ($COP): "))

        Total_Venta = Valor_Venta + Total_Venta

        Comision = Total_Venta * 0.1

    print(f"El vendedor número {i} vendió un total de {Total_Venta} $COP. Por lo tanto recibirá un extra de {Comision} $COP, correspondiente a un 10% de comisión sobre las ventas.")

print("El programa se completó")