# --- EXERCÍCIO: NÚMEROS ÍMPARES COM PASSO ---

# range(início, fim, passo)
# Começamos no 1.
# Vamos até o 21 (para incluir o 20, se fosse o caso).
# O passo '2' diz ao Python: "pule de 2 em 2" (1, 3, 5...)
impares = range(1, 21, 2)

for numero in impares:
    print(numero)