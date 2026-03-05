nome = "ada lovelace"
print(nome.title())

# O método .title() transforma a primeira letra de cada palavra em maiúscula
# e todas as outras letras em minúscula.
# Resultado esperado: Ada Lovelace
# =====================================================
#--------------------------------------------------
# Concatenando string
primeiro_nome = "Rafael"
sobrenome = "Lacerda"
nome_completo = primeiro_nome + "" + sobrenome

print(nome_completo)
print("Olá, " + nome_completo.title() + "!") #Formatação elegante

#ex 02:

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!" # u
print(message) # v

#Esse código também exibe a mensagem “Hello, Ada Lovelace!”, mas armazenar a mensagem em uma variável em u deixa a instrução print final em v muito mais simples

# =====================================================
# Espaços em branco em strings com tabulações ou quebras de linha

#Tabulação(TAB OU ESPAÇO)
print("Python")
#SAIDA: PYTHON
print("\tPython")
#SAIDA:     Python
# função \t é um tab ou espaço

#Quebra linha
#Função \n quebra linha.
print("Languages:\nPython\nC\nJavaScript")

#podemos combinar tabulações e quebras de linha em uma única string.
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Languages:
#   Python
#   C
#   JavaScript

# =====================================================
# GUIA COMPLETO: MANIPULAÇÃO DE STRINGS (TEXTOS)
# =====================================================

# 1. VARIAVEIS E REATRIBUIÇÃO
mensagem = "Olá, mundo!"
print(mensagem)

mensagem = "Nova mensagem na mesma variável"
print(mensagem)

# -----------------------------------------------------
# 2. ALTERAR MAIÚSCULAS/MINÚSCULAS
nome = "ada lovelace"

# .title() -> Primeira letra de cada palavra em MAIÚSCULA.
# Ideal para: Nomes próprios e títulos.
print(nome.title())  # Saída: Ada Lovelace

# .upper() -> TUDO EM MAIÚSCULA.
# Ideal para: Destacar avisos ou siglas.
print(nome.upper())  # Saída: ADA LOVELACE

# .lower() -> tudo em minúscula.
# Essencial para padronizar e-mails e logins no sistema.
print(nome.lower())  # Saída: ada lovelace

# -----------------------------------------------------
# 3. LIMPEZA DE ESPAÇOS EM BRANCO (STRIP)
linguagem = "  python  "

# .strip() -> Remove espaços inúteis do INÍCIO e do FIM.
# Evita erros se o usuário apertar espaço sem querer.
print(linguagem.strip())  # Saída: "python"

# .lstrip() -> Remove espaços apenas da ESQUERDA (Left).
print(linguagem.lstrip())

# .rstrip() -> Remove espaços apenas da DIREITA (Right).
print(linguagem.rstrip())

#No mundo real, essas funções de remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-las em um programa.

# -----------------------------------------------------
# 4. TRUQUE: EMPILHANDO MÉTODOS
# Você pode limpar o espaço E arrumar o título na mesma linha:
usuario = "  jOãO sILVA  "
print(usuario.strip().title()) # Saída: "João Silva"

#--------------------------------------------------------------
# O método lower() é particularmente útil para armazenar dados. Muitas vezes, você não vai querer confiar no fato de seus usuários fornecerem letras maiúsculas ou minúsculas, portanto fará a conversão das strings para letras minúsculas antes de armazená-las. Então, quando quiser exibir a informação, usará o tipo de letra que fizer mais sentido para cada string.