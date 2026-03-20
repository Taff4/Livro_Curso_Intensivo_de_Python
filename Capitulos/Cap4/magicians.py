# --- CONCEITO BÁSICO: O LAÇO 'FOR' ---
magicians = ['alice', 'david', 'carolina']

# O livro ensina a escolher nomes que façam sentido:
# 'for item_singular in lista_plural:'
for magician in magicians:
    print(magician)

# --- EXEMPLO 1: NOMEAÇÃO DE VARIÁVEIS ---
# O autor enfatiza que usar nomes descritivos ajuda a entender o código.
# (Estes são apenas exemplos de como estruturar o início de um loop)
"""
for cat in cats:                # Para cada gato na lista de gatos
for dog in dogs:                # Para cada cachorro na lista de cachorros
for item in list_of_items:      # Para cada item na lista de itens
"""

# --- EXEMPLO 2: PERSONALIZANDO MENSAGENS ---
print("\n--- Exemplo 2 ---")
for magician in magicians:
    # Usando o método .title() para capitalizar nomes próprios
    # Dica: O livro recomenda f-strings em vez de concatenar com '+'
    print(f"{magician.title()}, that was a great trick!")

# --- EXEMPLO 3: MÚLTIPLAS LINHAS DENTRO DO LOOP ---
print("\n--- Exemplo 3 ---")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # O '\n' no final cria uma linha em branco após cada iteração do bloco
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# --- EXEMPLO 4: AÇÕES APÓS O LOOP ---
print("--- Exemplo 4 ---")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Esta linha NÃO está indentada, então ela só executa UMA VEZ,
# após o Python terminar de percorrer toda a lista.
print("Thank you, everyone. That was a great magic show!")