# --- 1. ALTERANDO UM ITEM (SUBSTITUIÇÃO) ---
# Funciona como trocar um objeto de uma gaveta por outro.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'  # O Python vai na gaveta 0 e troca 'honda' por 'ducati'
print(motorcycles)

# --- 2. O MÉTODO append() (ACRESCENTAR NO FINAL) ---
# Imagine que a lista é uma fila. O append() coloca alguém no final da fila.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # Adiciona ao final sem mexer em quem já está lá
print(motorcycles)

# --- 3. O MÉTODO insert() (INSERIR EM QUALQUER LUGAR) ---
# Diferente do append, aqui você escolhe a posição.
# Quem estava lá é empurrado para a direita.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # Coloca 'ducati' na posição 0 e empurra o resto
print(motorcycles)

# --- 4. A INSTRUÇÃO del (APAGAR PARA SEMPRE) ---
# Use quando você quer jogar algo no lixo e não vai mais precisar dessa informação.
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0] # Remove quem está na posição 0. Acabou, sumiu!
print(motorcycles)

# --- 5. O MÉTODO pop() (REMOVER E GUARDAR) ---
# Imagine uma pilha de pratos. O pop() tira o último prato da pilha e te entrega.
motorcycles = ['honda', 'yamaha', 'suzuki']
# Aqui tiramos 'suzuki' da lista e guardamos na variável 'popped_motorcycle'
popped_motorcycle = motorcycles.pop()
print(motorcycles)       # A lista agora só tem dois itens
print(popped_motorcycle) # Aqui está o item que "pulou" da lista

# --- 6. UTILIDADE DO pop() (EXEMPLO PRÁTICO) ---
# Serve para quando você quer tirar algo da lista mas quer usar o nome em uma frase.
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() # Tira o último e guarda
print("A última moto que eu tive foi uma " + last_owned.title() + ".")

# --- 7. O MÉTODO remove() (REMOVER POR VALOR/NOME) ---
# Use quando você não sabe a posição (o índice), mas sabe o nome do que quer tirar.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati' # Guardamos o nome do que queremos tirar
motorcycles.remove(too_expensive) # O Python procura 'ducati' e remove
print(motorcycles)
print("\nA " + too_expensive.title() + " é muito cara para mim.")