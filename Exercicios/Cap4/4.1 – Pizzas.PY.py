"""
Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez
de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na
saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas
sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo,
Eu realmente adoro pizza!
"""

# Criamos uma lista com os nomes das pizzas (plural)
pizzas = ["portuguesa", "frango catupiry", "atum"]

# O laço 'for' percorre cada item da lista.
# O padrão recomendado é: for item_singular in lista_plural:
# Aqui, mudei de 'nomes' para 'pizza' para ficar mais claro.
for pizza in pizzas:
    # Esta linha está indentada, então ela repete para cada pizza da lista.
    # Usamos f-string para inserir a variável dentro da frase.
    # O método .title() garante que o nome comece com letra maiúscula.
    print(f"Gosto de pizza de {pizza.title()}.")

# Esta linha está FORA do laço (sem recuo à esquerda).
# Por isso, ela só será executada uma vez, depois que o laço terminar.
print("\nEu realmente adoro pizza!")