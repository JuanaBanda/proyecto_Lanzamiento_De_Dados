import random

dado1 = 0
dado2 = 0
valoresDado1 = ""
valoresDado2 = ""

# Repetir hasta que ambos dados sean 6
while dado1!=6 or dado2!=6:
  # Lanzar los 2 dados
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  # Concatenar los valores obtenidos a los obtenidos hasta el momento
  valoresDado1 += str(dado1)
  valoresDado2 += str(dado2)
  
# Mostrar finalmente todos los lanzamientos realizados
print("Dado 1: " + valoresDado1)
print("Dado 2: " + valoresDado2)