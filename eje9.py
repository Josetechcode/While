# DISPLAY TITLE
print("*** PROGRAMA QUE MUESTRA EL RESULTADO DEL PROCESO DE SELECCIÓN DEL REPRESENTANTE ESTUDIANTIL ***\n\nNota: Para ganar las elecciones el candidato debe alcanzar el 51 porciento de los votos")

# PROMTING THE USER HOW MANY PEOPLE ARE VOTING
Voters = int(input("Cuántas personas van a votar: "))

i = 0
A = 0
B = 0
C = 0

while i < Voters:
  i += 1

  # PROMTING THE VOTER WHO THEY'RE VOTING FOR
  Choice = int(input("Por cual candidato va a votar:\n1. Candidato A.\n2. Candidato B.\n3. Candidato C.\n"))

  if Choice == 1:
    A += 1 # ADDING UP VOTES TO CANDIDATE "A"
    print (f"Se ha registrado el voto número {i}.")
  elif Choice == 2:
    B += 1 # ADDING UP VOTES TO CANDIDATE "B"
    print (f"Se ha registrado el voto número {i}.")
  elif Choice == 3:
    C += 1 # ADDING UP VOTES TO CANDIDATE "C"
    print (f"Se ha registrado el voto número {i}.")

Total = A + B + C # ADDING UP THE TOTAL OF THE VOTES

if (A/Total)*100 >= 51:
  print(f"El candidato A fue el ganador con {A} voto(s).\nEl candidato B obtuvo {B} voto(s).\nEl candidato C obtuvo {C} voto(s).")
elif (B/Total)*100 >= 51:
  print(f"El candidato B fue el ganador con {B} voto(s).\nEl candidato A obtuvo {A} voto(s).\nEl candidato C obtuvo {C} voto(s).")
elif (C/Total)*100 >= 51:
  print(f"El candidato C fue el ganador con {C} voto(s).\nEl candidato A obtuvo {A} voto(s).\nEl candidato B obtuvo {B} voto(s).")
else:
  print(f"Ningún candidato obtuvo el 51% de las votaciones.\nEl candidato A obtuvo {A} voto(s).\nEl candidato B obtuvo {B} voto(s).\nEl candidato C obtuvo {C} voto(s).")

"""  print("la elección se repite en una segunda vuelta con los candidatos que quedaron en primero y segundo lugar.")
  
  if A > B and A > C:
    if B > C:
      print("Los candidatos que van a segunda vuelta son A y B.")
      i = 0
      while i < Voters:
        i += 1
        Choice = int(input("Por cual candidato va a votar:\n1. Candidato A.\n2. Candidato B.\n"))

        if Choice == 1:
          A += 1 # ADDING UP VOTES TO CANDIDATE "A"
          print (f"Se ha registrado el voto número {i}.")
        elif Choice == 2:
          B += 1 # ADDING UP VOTES TO CANDIDATE "B"
          print (f"Se ha registrado el voto número {i}.")
          
    elif C > B:
      print("Los candidatos que van a segunda vuelta son A y C.")
      i = 0
      while i < Voters:
        i += 1
        Choice = int(input("Por cual candidato va a votar:\n1. Candidato A.\n2. Candidato C.\n"))

        if Choice == 1:
          A += 1 # ADDING UP VOTES TO CANDIDATE "A"
          print (f"Se ha registrado el voto número {i}.")
        elif Choice == 2:
          C += 1 # ADDING UP VOTES TO CANDIDATE "C"
          print (f"Se ha registrado el voto número {i}.")

  elif B > A and B > C:
    if C > A:
      print("Los candidatos que van a segunda vuelta son B y C.")
      i = 0
      while i < Voters:
        i += 1
        Choice = int(input("Por cual candidato va a votar:\n1. Candidato B.\n2. Candidato C.\n"))

        if Choice == 1:
          B += 1 # ADDING UP VOTES TO CANDIDATE "B"
          print (f"Se ha registrado el voto número {i}.")
        elif Choice == 2:
          C += 1 # ADDING UP VOTES TO CANDIDATE "C"
          print (f"Se ha registrado el voto número {i}.")

  else:
    if A == B:
      print("Por empate entre candidatos A y B la elección se declara nula.\nEl proceso de votación se debe realizar nuevamente desde cero.")
    elif A == C:
      print("Por empate entre candidatos A y C la elección se declara nula.\nEl proceso de votación se debe realizar nuevamente desde cero.")
    elif B == C:
      print("Por empate entre candidatos B y C la elección se declara nula.\nEl proceso de votación se debe realizar nuevamente desde cero.") """