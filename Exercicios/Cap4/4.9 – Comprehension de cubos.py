"""
Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
"""

# --- EXERCÍCIO: CUBOS COM LIST COMPREHENSION ---

print("\n--- List Comprehension ---")

# A estrutura funciona assim:
# [o que fazer com o valor | para cada valor | em qual intervalo]
cubos = [value**3 for value in range(1, 11)]

# Exibindo a lista resultante
print(cubos)