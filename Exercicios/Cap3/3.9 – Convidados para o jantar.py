"""
Trabalhando com um dos programas dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
informando o número de pessoas que você está convidando para o jantar.
"""
lista = ['Tim Maia', 'FBC', 'Djonga']

# Guardamos a base do convite em uma variável
convite = "você gostaria de trocar uma ideia comigo hoje?"
quantidade = len(lista)
# Exibimos usando a f-string para juntar o nome e o convite
print(f"Olá {lista[0]}, {convite}")
print(f"Olá {lista[1]}, {convite}")
print(f"Olá {lista[2]}, {convite}")

# Use assim (mais "Pythonico"):
print(f"Eu tenho {quantidade} convidados.")