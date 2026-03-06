"""Pense em pelo menos cinco lugares do mundo que
você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou."""

cidades = ['Tokyo', 'Florida', 'Salvador', 'Rio de Janeiro', 'Berlin']

# 1. Ordem original
print("Original:", cidades)

# 2. Ordem alfabética sem modificar a original (sorted)
print("Alfabética:", sorted(cidades))

# 3. Confirmando que a original continua igual
print("Original mantida:", cidades)

# 4. Ordem alfabética inversa sem modificar (sorted com reverse=True)
print("Alfabética Inversa:", sorted(cidades, reverse=True))

# 5. Confirmando que a original continua igual
print("Original mantida:", cidades)

# 6. Mudando a ordem com reverse() (Inverte a posição atual)
cidades.reverse()
print("Ordem Invertida:", cidades)

# 7. Voltando à ordem original com reverse()
cidades.reverse()
print("Voltou ao normal:", cidades)

# 8. Mudando para ordem alfabética definitiva com sort()
cidades.sort()
print("Alfabética definitiva:", cidades)

# 9. Mudando para alfabética inversa definitiva com sort(reverse=True)
cidades.sort(reverse=True)
print("Alfabética inversa definitiva:", cidades)