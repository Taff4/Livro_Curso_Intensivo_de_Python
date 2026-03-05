"""Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados para o
jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que você
encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
está em sua lista."""

lista = ['Tim Maia', 'FBC', 'Djonga']
convite = "você gostaria de trocar uma ideia comigo hoje?"

# Aviso de quem não vai e substituição
print(f'O convidado {lista[2]} não vai.')
lista[2] = 'Emicida'
print(f"{'-'*50}")
# --- O QUE FALTOU: O AVISO DA MESA ---
print("\nBoas notícias! Encontrei uma mesa de jantar maior!")
print(f"{'-'*50}")

# Inserindo novos convidados
lista.insert(0, 'Sabotagem')    # Início
lista.insert(2, 'Mano Brown')   # Agora no novo meio (índice 2)
lista.append('Don L')           # Final

# Exibindo os convites atualizados
print(f"Olá {lista[0].title()}, {convite}")
print(f"Olá {lista[1].title()}, {convite}")
print(f"Olá {lista[2].title()}, {convite}")
print(f"Olá {lista[3].title()}, {convite}")
print(f"Olá {lista[4].title()}, {convite}")
print(f"Olá {lista[5].title()}, {convite}")
