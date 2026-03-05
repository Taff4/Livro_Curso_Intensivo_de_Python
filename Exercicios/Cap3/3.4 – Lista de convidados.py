"""Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir
uma mensagem para cada pessoa, convidando-a para jantar."""

lista = ['Tim Maia', 'FBC', 'Djonga']

# Guardamos a base do convite em uma variável
convite = "você gostaria de trocar uma ideia comigo hoje?"

# Exibimos usando a f-string para juntar o nome e o convite
print(f"Olá {lista[0]}, {convite}")
print(f"Olá {lista[1]}, {convite}")
print(f"Olá {lista[2]}, {convite}")