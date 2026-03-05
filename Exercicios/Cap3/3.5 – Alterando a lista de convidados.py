"""Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar um
novo conjunto de convites. Você deverá pensar em outra pessoa para convidar."""

lista = ['Tim Maia', 'FBC', 'Djonga']

# Guardamos a base do convite em uma variável
convite = "você gostaria de trocar uma ideia comigo hoje?"

print(f'{'-'*50}')
print(f'O convidado {lista[2]} não vai.')
# Alterando um item:
lista[2] = 'Emicida'  # 'honda' foi substituída por 'ducati'
print(f'{'-'*50}')
# Exibimos usando a f-string para juntar o nome e o convite
print(f"Olá {lista[0]}, {convite}")
print(f"Olá {lista[1]}, {convite}")
print(f"Olá {lista[2]}, {convite}")



