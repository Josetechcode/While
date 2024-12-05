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

  Choice = 0
  while Choice != 1 and Choice != 2 and Choice != 3:
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
  print(f"El candidato A fue el ganador con {A} votos.\nEl candidato B obtuvo {B} votos.\nEl candidato C obtuvo {C} votos.")
elif (B/Total)*100 >= 51:
  print(f"El candidato B fue el ganador con {B} votos.\nEl candidato A obtuvo {A} votos.\nEl candidato C obtuvo {C} votos.")
elif (C/Total)*100 >= 51:
  print(f"El candidato C fue el ganador con {C} votos.\nEl candidato A obtuvo {A} votos.\nEl candidato B obtuvo {B} votos.")
else:
  print(f"Ningún candidato obtuvo el 51% de las votaciones.\nEl candidato A obtuvo {A} votos.\nEl candidato B obtuvo {B} votos.\nEl candidato C obtuvo {C} votos.")
  
  if A > B and A > C:
    if B > C:
      i = 0
      while i < Voters:
        i += 1

        Choice = 0
        while Choice != 1 and Choice != 2:
          # PROMTING THE VOTER WHO THEY'RE VOTING FOR
          Choice = int(input("Por cual candidato va a votar:\n1. Candidato A.\n2. Candidato B.\n"))

          if Choice == 1:
            A += 1 # ADDING UP VOTES TO CANDIDATE "A"
            print (f"Se ha registrado el voto número {i}.")
          elif Choice == 2:
            B += 1 # ADDING UP VOTES TO CANDIDATE "B"
            print (f"Se ha registrado el voto número {i}.")
          
      if A > B:
        print (f"El candidato A es el ganador con {A} votos")
      elif B > A:
        print (f"El candidato B es el ganador con {B} votos")
      else:
        print (f"El candidato A obtuvo {A} votos y el B obtuvo {B} votos. Dado que hay empate la elección se anula.")
    
    else:
      i = 0
      while i < Voters:
        i += 1

        Choice = 0
        while Choice != 1 and Choice != 3:
          # PROMTING THE VOTER WHO THEY'RE VOTING FOR
          Choice = int(input("Por cual candidato va a votar:\n1. Candidato A.\n3. Candidato C.\n"))

          if Choice == 1:
            A += 1 # ADDING UP VOTES TO CANDIDATE "A"
            print (f"Se ha registrado el voto número {i}.")
          elif Choice == 3:
            C += 1 # ADDING UP VOTES TO CANDIDATE "B"
            print (f"Se ha registrado el voto número {i}.")
          
      if A > C:
        print (f"El candidato A es el ganador con {A} votos")
      elif C > A:
        print (f"El candidato C es el ganador con {C} votos")
      else:
        print (f"El candidato A obtuvo {A} votos y el C obtuvo {C} votos. Dado que hay empate la elección se anula.")


else:
  i = 0
  while i < Voters:
    i += 1

    Choice = 0
    while Choice != 1 and Choice != 3:
      # PROMTING THE VOTER WHO THEY'RE VOTING FOR
      Choice = int(input("Por cual candidato va a votar:\n2. Candidato B.\n3. Candidato C.\n"))

      if Choice == 2:
        B += 1 # ADDING UP VOTES TO CANDIDATE "A"
        print (f"Se ha registrado el voto número {i}.")
      elif Choice == 3:
        C += 1 # ADDING UP VOTES TO CANDIDATE "B"
        print (f"Se ha registrado el voto número {i}.")
          
      if B > C:
        print (f"El candidato A es el ganador con {A} votos")
      elif C > A:
        print (f"El candidato C es el ganador con {C} votos")
      else:
        print (f"El candidato A obtuvo {A} votos y el C obtuvo {C} votos. Dado que hay empate la elección se anula.")