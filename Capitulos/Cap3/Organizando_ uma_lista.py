# =====================================================================
# ORGANIZANDO UMA LISTA (Capítulo 3)
# =====================================================================

cars = ['bmw', 'audi', 'toyota', 'subaru']

# --- 1. MÉTODO sort() ---
# O método sort() ordena a lista em ordem alfabética de forma PERMANENTE.
# Você não consegue mais voltar à ordem original depois de usá-lo.
cars.sort()
print("1. Ordem alfabética permanente:")
print(cars)

# --- 2. MODO REVERSO DO sort() ---
# Você pode passar o argumento 'reverse=True' dentro do sort().
# Isso também altera a lista de forma PERMANENTE para a ordem alfabética inversa.
cars.sort(reverse=True)
print("\n2. Ordem alfabética inversa permanente:")
print(cars)

# ---------------------------------------------------------------------

# --- 3. FUNÇÃO sorted() ---
# Diferente do sort(), a função sorted() é TEMPORÁRIA.
# Ela exibe a lista ordenada para você, mas não mexe na ordem original do arquivo.
cars = ['bmw', 'audi', 'toyota', 'subaru'] # Reiniciando a lista

print("\n3. Comparando original vs sorted():")
print("Lista original:")
print(cars)

print("Lista exibida com sorted() (temporário):")
print(sorted(cars))

print("Lista original novamente (continua igual):")
print(cars)

# ---------------------------------------------------------------------

# --- 4. MÉTODO reverse() ---
# ATENÇÃO: O reverse() NÃO coloca em ordem alfabética inversa.
# Ele apenas "capota" a lista, invertendo a ordem dos itens de trás para frente.
# Também é uma mudança PERMANENTE.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n4. Usando o reverse() (Inverter a fila):")
print(cars)
cars.reverse()
print(cars)

# ---------------------------------------------------------------------

# --- 5. FUNÇÃO len() ---
# Serve para descobrir o tamanho da lista (quantos itens ela tem).
# Muito útil quando você tem listas gigantes com milhares de itens.
cars = ['bmw', 'audi', 'toyota', 'subaru']
tamanho = len(cars)
print("\n5. Tamanho da lista:")
print(f"A lista possui {tamanho} itens.")