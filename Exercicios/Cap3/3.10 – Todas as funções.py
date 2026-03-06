"""
Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
uma lista contendo esses itens e então utilize cada função apresentada neste
capítulo pelo menos uma vez.
"""
# --- 1. CRIANDO A LISTA E ALTERANDO ITENS ---
# Posições (Índices): 0: 'PS4', 1: 'PS2', 2: 'XBOX360', 3: 'PC'
games = ['PS4', 'PS2', 'XBOX360', 'PC']
print(f"Lista Original: {games}")

# Trocando um item específico pelo índice
games[0] = 'Nintendo Switch'
print(f"1. Após trocar PS4 por Switch: {games}")


# --- 2. O MÉTODO append() (ADICIONAR AO FINAL) ---
games.append('GameBoy')
print(f"2. Adicionado ao final: {games}")


# --- 3. O MÉTODO insert() (INSERIR EM POSIÇÃO ESPECÍFICA) ---
# Coloca 'Atari' na posição 1 e empurra os outros para a direita
games.insert(1, 'Atari')
print(f"3. Inserido Atari na posição 1: {games}")


# --- 4. A INSTRUÇÃO del (REMOVER PERMANENTEMENTE) ---
del games[2] # Remove quem estiver na posição 2 (neste caso, o PS2)
print(f"4. Após deletar posição 2: {games}")


# --- 5. O MÉTODO pop() (REMOVER E "PULAR" PARA UMA VARIÁVEL) ---
# Remove o último item da lista, mas permite que você o use depois
game_removido = games.pop()
print(f"5. Lista após pop: {games}")
print(f"   Item que saiu da lista: {game_removido}")


# --- 6. O MÉTODO remove() (REMOVER POR NOME/VALOR) ---
# Útil quando você não sabe onde o item está, mas sabe o nome dele
caro_demais = 'PC'
games.remove(caro_demais)
print(f"6. Após remover '{caro_demais}': {games}")


# --- 7. O MÉTODO sort() (ORDEM ALFABÉTICA DEFINITIVA) ---
# Altera a lista original para sempre
games.sort()
print(f"7. Ordem alfabética (permanente): {games}")

# Ordem alfabética inversa definitiva
games.sort(reverse=True)
print(f"   Ordem alfabética inversa (permanente): {games}")


# --- 8. A FUNÇÃO sorted() (ORDEM ALFABÉTICA TEMPORÁRIA) ---
# Reiniciando a lista para testar
meus_games = ['Zelda', 'Mario', 'Metroid', 'Halo']
print(f"\n8. Original antes do sorted: {meus_games}")
print(f"   Exibindo com sorted(): {sorted(meus_games)}")
print(f"   Lista continua original: {meus_games}")


# --- 9. O MÉTODO reverse() (INVERTER A FILA) ---
# Não é ordem alfabética, ele apenas "espelha" a lista atual
meus_games.reverse()
print(f"9. Lista 'capotada' (reverse): {meus_games}")


# --- 10. A FUNÇÃO len() (TAMANHO DA LISTA) ---
quantidade = len(meus_games)
print(f"10. No total, eu tenho {quantidade} games na minha lista.")