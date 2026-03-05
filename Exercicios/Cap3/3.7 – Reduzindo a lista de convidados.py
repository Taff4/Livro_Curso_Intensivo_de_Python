"""
Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas pessoas
para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na
lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
lista vazia no final de seu programa.
"""

lista = ['Sabotagem', 'Tim Maia', 'Mano Brown', 'FBC', 'Emicida', 'Don L']
convite = "você ainda está convidado para trocar uma ideia!"

print(f"\nPéssimas notícias! A mesa não chegará a tempo. Só tenho 2 vagas.")
print(f"{'-'*50}")

# Removendo até sobrarem 2 (Tiramos 4 pessoas)
# O pop() sem número tira sempre o ÚLTIMO da lista.
removido = lista.pop()
print(f"Sinto muito, {removido.title()}, não vai dar desta vez.")

removido = lista.pop()
print(f"Sinto muito, {removido.title()}, não vai dar desta vez.")

removido = lista.pop()
print(f"Sinto muito, {removido.title()}, não vai dar desta vez.")

removido = lista.pop()
print(f"Sinto muito, {removido.title()}, não vai dar desta vez.")

print(f"{'-'*50}")

# Avisando os dois que sobraram
print(f"Olá {lista[0].title()}, {convite}")
print(f"Olá {lista[1].title()}, {convite}")

# AGORA O PASSO FINAL DO EXERCÍCIO: Deixar a lista vazia
del lista[0]
del lista[0] # Note que ao deletar o [0], o que era [1] passa a ser o novo [0]!

# Verificando se está vazia
print(f"\nLista final: {lista}")