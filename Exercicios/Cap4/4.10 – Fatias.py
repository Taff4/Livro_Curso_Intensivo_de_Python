"""
Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três
itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir
os três últimos itens da lista.
"""
# ==============================================================================
# EXERCÍCIO DE FATIAMENTO (SLICING) - CAPÍTULO 4
# ==============================================================================

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 1. Os três primeiros (0, 1, 2)
print('Os três primeiros itens da lista são:')
print(players[0:3])

# 2. Três itens do meio (1, 2, 3)
# Note que a diferença entre os índices (4 - 1) é igual a 3,
# garantindo a quantidade de itens pedida.
print('\nTrês itens do meio da lista são:')
print(players[1:4])

# 3. Os três últimos
# O índice negativo começa de trás para frente, e o ':' garante que seja uma fatia.
print('\nOs três últimos itens da lista são:')
print(players[-3:])