"""
Para copiar uma lista, podemos criar uma fatia que inclua a lista original
inteira omitindo o primeiro e o segundo índices ([:]). Isso diz a Python
para criar uma lista que começa no primeiro item e termina no último,
gerando uma cópia da lista toda.
"""

# ==============================================================================
# COPIANDO UMA LISTA INTEIRA (USANDO FATIAS [:])
# ==============================================================================

# 1. A MANEIRA CORRETA DE COPIAR
# Ao usar [:] sem números, o Python cria uma cópia real e independente.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# 2. PROVANDO QUE SÃO LISTAS DIFERENTES
# Vamos adicionar comidas diferentes em cada lista para testar.
my_foods.append('cannoli')      # Adiciona apenas na minha lista
friend_foods.append('sorvete')  # Adiciona apenas na lista do amigo

print("Minhas comidas favoritas são:")
print(my_foods)
# Resultado esperado: ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nAs comidas favoritas do meu amigo são:")
print(friend_foods)
# Resultado esperado: ['pizza', 'falafel', 'carrot cake', 'sorvete']


# ------------------------------------------------------------------------------
# ATENÇÃO: POR QUE "friend_foods = my_foods" NÃO FUNCIONA?
# ------------------------------------------------------------------------------
"""
Se você fizer: friend_foods = my_foods (sem o [:]), 
você NÃO está criando uma cópia. 

Você está dizendo ao Python que as duas variáveis apontam para a MESMA lista 
na memória do computador. 

Se você adicionar um item em 'my_foods', ele aparecerá automaticamente 
em 'friend_foods', porque, para o Python, elas viraram a mesma coisa.
"""

# Exemplo do erro (CUIDADO):
lista_a = [1, 2, 3]
lista_b = lista_a # Isso NÃO é uma cópia!

lista_a.append(4)
print("\n--- TESTE DE ERRO ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}") # A lista B também terá o número 4!