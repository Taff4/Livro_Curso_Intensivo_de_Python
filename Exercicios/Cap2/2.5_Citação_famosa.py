print(f"{'Exe 2,5' :=^50}")

# Encontre uma citação de uma pessoa famosa que você admire. Exiba a citação e o nome do autor.Sua saída deverá ter a aparência a
# seguir, incluindo as aspas

# Armazenamos os dados nas variáveis
autor = 'Hebe de Bonafini'
citacao = 'A única luta que se perde é aquela que se abandona e nós nunca, nunca abandonamos a luta.'

# EXPLICAÇÃO DO 'f':
# 1. O 'f' antes das aspas significa "FORMAT".
# 2. Ele avisa ao Python: "Ei, não trate isso apenas como um texto comum."
# 3. Ele habilita as chaves { } para que o Python INTERPOLE (insira) o valor das variáveis.
print(f'{autor} certa vez disse: "{citacao}"')

# Se você esquecesse o 'f', o Python imprimiria literalmente:
# {autor} certa vez disse: "{citacao}"
