"""
Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais, interrompa
pressionando CTRL-C ou feche a janela de saída.)
"""

# --- EXERCÍCIO: UM MILHÃO ---

# 1. Para incluir exatamente 1.000.000, o range deve ir até 1.000.001
# 2. Não é estritamente necessário converter para list() dentro do 'for',
# pois o próprio range() já é um objeto iterável muito mais eficiente em memória.
numeros = range(1, 1000001)

for i in numeros:
    print(i)