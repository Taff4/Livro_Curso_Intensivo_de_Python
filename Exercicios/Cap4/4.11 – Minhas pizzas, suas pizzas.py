"""
Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja
armazenada na lista apropriada.
"""

# ==============================================================================
# EXERCÍCIO: MINHAS PIZZAS, SUAS PIZZAS (PÁGINA 97)
# ==============================================================================

# 1. Criando a lista original
my_pizzas = ['calabresa', 'frango', 'atum']

# 2. Fazendo uma cópia real da lista usando [:]
friend_pizzas = my_pizzas[:]

# 3. Adicionando uma nova pizza à lista original
my_pizzas.append('chocolate')

# 4. Adicionando uma pizza diferente à lista do amigo
friend_pizzas.append('mussarela')

# 5. Provando que as listas são diferentes com laços 'for'

print("Minhas pizzas favoritas são:")
# Para cada 'pizza' dentro da lista 'my_pizzas':
for pizza in my_pizzas:
    print("- " + pizza.title())

print("\nAs pizzas favoritas do meu amigo são:")
# Para cada 'pizza' dentro da lista 'friend_pizzas':
for pizza in friend_pizzas:
    print("- " + pizza.title())

# ==============================================================================
# EXPLICAÇÃO RÁPIDA PARA O SEU CADERNO:
# ==============================================================================
# - Usamos 'for pizza in lista:' porque o Python já entende que deve pegar
#   um item por vez. Não precisamos do range() aqui.
# - O 'pizza' é uma variável temporária que criamos na hora; ela representa
#   o item atual que o laço está lendo.
# - Como usamos o [:] lá no início, a 'mussarela' só aparece na lista do amigo
#   e o 'chocolate' só aparece na sua.