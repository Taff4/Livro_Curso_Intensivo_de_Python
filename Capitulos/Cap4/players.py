# ==============================================================================
# ESTUDO DE FATIAMENTO DE LISTAS (SLICING) - CAPÍTULO 4
# ==============================================================================

# Criamos nossa lista inicial de jogadores
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 1. FATIANDO (Pegando um intervalo específico)
# O Python pega do primeiro índice até um antes do último índice indicado.
# Aqui ele pega as posições 1, 2 e 3 (índice 4 fica de fora).
print("Fatia do índice 1 ao 3:")
print(players[1:4]) 

# 2. PRIMEIRO ITEM OMITIDO
# Se você não colocar o número antes dos dois pontos [:4], 
# o Python entende que deve começar do início da lista (índice 0).
print("\nDo início até o índice 3:")
print(players[:4])

# 3. ÚLTIMO ITEM OMITIDO
# Se você não colocar o número depois dos dois pontos [2:],
# o Python pega do índice indicado até o final da lista, não importa o tamanho.
print("\nDo índice 2 até o final:")
print(players[2:])

# 4. USANDO ÍNDICES NEGATIVOS
# O sinal de menos faz o Python contar de trás para frente.
# [-3:] significa: "comece a contar 3 posições antes do fim e vá até o final".
print("\nOs últimos 3 jogadores da lista:")
print(players[-3:])

# ------------------------------------------------------------------------------
# PERCORRENDO UMA FATIA COM UM LAÇO (FOR)
# ------------------------------------------------------------------------------
# Podemos usar o 'for' para trabalhar apenas com uma parte da lista, 
# em vez de usar a lista inteira.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team:")

# O laço 'for' abaixo percorre apenas a fatia [:3] (índices 0, 1 e 2)
for player in players[:3]:
    # O .title() deixa a primeira letra maiúscula
    print(player.title())

"""
Ao trabalhar com grandes volumes de dados, as fatias são essenciais 
para processar informações em "pedaços" menores e mais fáceis de gerenciar.
"""