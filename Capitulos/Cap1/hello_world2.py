# --- PARTE 1: O Computador interage com você ---
# O comando 'input' exibe uma mensagem e PAUSA o programa.
# Tudo o que você digitar será guardado dentro da variável 'nome_usuario'.

nome_usuario = input("Olá! Qual é o seu nome? ")

# --- PARTE 2: Usando a informação recebida ---
# Agora pegamos o que você digitou e montamos uma frase personalizada.
# Usamos o 'f' antes das aspas para "chamar" a variável dentro das chaves {}.

mensagem_boas_vindas = f"Prazer em te conhecer, {nome_usuario}! Seja bem-vindo ao Python."

print("\n--- Resultado da Interação ---")

print(mensagem_boas_vindas)

# --- PARTE 3: Um pequeno desafio de lógica ---
# Vamos perguntar sua idade.
# Importante: O input sempre recebe TEXTO.
# Se quisermos tratar como número depois, precisamos converter (mas vamos manter simples por enquanto).

idade = input("Quantos anos você tem? ")

print(f"Legal! Então você tem {idade} anos e já está começando a programar. Nada mal, {nome_usuario}!")