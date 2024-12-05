# DISPLAY TITLE
print("*** PROGRAMA QUE CALCULA EL PROMEDIO PONDERADO ***")

# PROMPT THE USER HOW MANY STUDENT THEY ARE ENTERING
Num = float(input("Cuántos estudiantes va a ingresar: "))

# PROMPT THE USER HOW MANY CREDIT THE SUBJECT HAS
Fun_Cred = float(input("Ingrese cantidad de créditos de fundamentos: "))
BD_Cred = float(input("Ingrese cantidad de créditos de BD: "))
Etica_Cred = float(input("Ingrese cantidad de créditos de Ética: "))

i = 0 #  STUDENTS COUNTER

while(i < Num): #  AS LONG AS "i" IS LESS THAN "Num" THE WHILE-LOOP WILL KEEP RUNNING
  i += 1
  # PROMPTING THE GRADE
  Fun_Nota = float(input(f"Ingrese nota de Fundamentos del estudiante número {i}: "))
  
  # PROMPTING THE GRADE
  BD_Nota = float(input(f"Ingrese nota de BD del estudiante número {i}: "))
  
  # PROMPTING THE GRADE
  Etica_Nota = float(input(f"Ingrese nota de Ética del estudiante número {i}: "))
  
  # DISPLAYING THE AVERAGE GRADE 
  print(f"El promedio ponderado del estudiante número {i} es", (Fun_Nota * Fun_Cred + BD_Nota * BD_Cred + Etica_Nota * Etica_Cred) / (Fun_Cred + BD_Cred + Etica_Cred),".")

# WRAPPING UP THE PROGRAM
print("El programa ha terminado.\n¡Gracias!")