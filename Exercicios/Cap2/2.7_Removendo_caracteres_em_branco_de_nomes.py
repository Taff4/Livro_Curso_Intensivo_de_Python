# Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembrese de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
# Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados.
# Em seguida, exiba o nome usando cada uma das três funções de remoção de espaços: lstrip(), rstrip() e strip().

print(f"{'Removendo caracteres em branco de nomes':=^50}")

# 1. Armazenar: Criamos um nome "sujo" com espaços, tabulação (\t) e quebra de linha (\n)
# Nota: O Python trata esses caracteres como dados reais dentro da string.
nome_sujo = "\t Eric Mattheus \n"

# 2. Exibição Original (mostrando os espaços e quebras)
# Usamos aspas simples extras '' para delimitar visualmente onde o espaço termina.
print("1. Nome original (com espaço e quebras):")
print(f"'{nome_sujo}'")

print("-" * 50)

# 3. AS TRÊS FUNÇÕES DE LIMPEZA (MÉTODOS DE STRING)

# lstrip() -> "Left Strip" (Limpa a ESQUERDA)
# Remove o \t e os espaços iniciais, mas mantém o \n no final.
print(f"2. lstrip() - Remove apenas o início:\n'{nome_sujo.lstrip()}'")

# rstrip() -> "Right Strip" (Limpa a DIREITA)
# Remove o \n e os espaços finais. Note que o texto 'sobe' no console.
print(f"3. rstrip() - Remove apenas o fim:\n'{nome_sujo.rstrip()}'")

# strip() -> Limpeza Completa (Início e Fim)
# É a função mais utilizada para garantir que o dado esteja "limpo".
print(f"4. strip() - Remove ambos os lados:\n'{nome_sujo.strip()}'")

# ---------------------------------------------------------
# EXPLICAÇÃO TÉCNICA E DICAS DE USO:
# ---------------------------------------------------------

# QUANDO USAR?
# Essencial para COMPARAR strings ou salvar em bancos de dados.
# Exemplo: if nome_sujo.strip() == "Eric Mattheus":
# Sem o .strip(), essa comparação seria FALSA por causa dos espaços invisíveis.

print("-" * 50)

# DICA DE OURO: ENCADEAMENTO (METHOD CHAINING)
# O Python executa da esquerda para a direita: primeiro limpa (strip), depois formata (title).
nome_final = nome_sujo.strip().title()
print(f"\n5. Exemplo de Encadeamento (strip + title):\n'{nome_final}'")

# POR QUE O 'f' NO PRINT?
# O prefixo 'f' (f-string) faz o Python "interpolar" o código dentro das chaves {}.
# É mais performático e fácil de ler do que concatenar com + ou usar o antigo .format().