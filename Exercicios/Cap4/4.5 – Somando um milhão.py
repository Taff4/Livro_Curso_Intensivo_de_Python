"""
Crie uma lista de números de um a um milhão e, em
seguida, use min() e max() para garantir que sua lista realmente começa em um e
termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
que Python é capaz de somar um milhão de números.
"""

# --- EXERCÍCIO: ESTATÍSTICAS COM UM MILHÃO ---

# Criamos o intervalo de 1 até 1.000.000
# O Python gera esses números de forma extremamente eficiente.
numeros = range(1, 1000001)

# min() encontra o menor valor da lista/intervalo
# Corrigido: Adicionado o parêntese ")" que faltava após 'numeros'
print(f"Menor valor: {min(numeros)}")

# max() encontra o maior valor
print(f"Maior valor: {max(numeros)}")

# sum() soma todos os itens.
# Você verá que o Python faz isso quase instantaneamente!
print(f"Soma total:  {sum(numeros)}")