print(f"{'Exe 2.4' :=^50}")

# --- ENTRADA ---
# O Python pausa a execução e espera o usuário digitar algo.
nome_completo = input('Digite seu nome completo: ')

# --- SAÍDA ---

# 1. .title() -> Capitaliza a primeira letra de CADA palavra.
# Ideal para nomes próprios como "Eric Silva".
print(f'Seu nome em formato de título: {nome_completo.title()}')

# 2. .lower() -> Transforma absolutamente tudo em minúsculo.
# Muito usado para padronizar e-mails e buscas em bancos de dados.
print(f'Seu nome em letras minúsculas: {nome_completo.lower()}')

# 3. .upper() -> Transforma tudo em MAIÚSCULO.
# Útil para cabeçalhos, alertas ou destacar nomes em documentos.
print(f'Seu nome em letras maiúsculas: {nome_completo.upper()}')