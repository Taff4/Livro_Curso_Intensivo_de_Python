# --- EXERCÍCIO: MÚLTIPLOS DE 3 ---

# Criamos o intervalo começando em 3, indo até 30 (limite 31)
# O passo 3 garante que apenas os múltiplos sejam selecionados
multiplos_de_tres = range(3, 31, 3)

# O laço percorre a lista gerada e exibe cada valor
for numero in multiplos_de_tres:
    print(numero)