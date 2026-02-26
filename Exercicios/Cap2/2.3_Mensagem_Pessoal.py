print(f"{'Exe 2.3 .format()' :=^50}")

#Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa.
# Sua mensagem deve ser simples, como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.

#Armazenar
nome = (input('Digite seu nome: '))
pergunta = 'você gostaria de aprender um pouco de Python hoje?”.'

#exibir
print('Alô {}, {}'.format(nome, pergunta))

#============================================================================
# --- MODO MODERNO (f-string) ---
# O 'f' antes das aspas diz ao Python para "olhar" dentro das chaves {} e processar o que está lá.
# É a forma mais rápida e legível.
print(f"{'MODO MODERNO (f-string)' :=^50}")

nome = input('Digite seu nome: ')
pergunta = 'você gostaria de aprender um pouco de Python hoje?'

# Exemplo com f-string: A variável entra direto no texto.
# No PyCharm, o {nome} ganha uma cor diferente, facilitando a leitura.
print(f"Alô {nome}, {pergunta}")


# --- MODO ANTIGO (.format) ---
# Aqui você cria "buracos" {} e depois preenche com a lista de variáveis no final.
# print('Alô {}, {}'.format(nome, pergunta))

#=========================================================================================
#Quando usar um ou outro?
#1. Use f-strings em 99% dos casos: Sempre que você estiver escrevendo o texto e as variáveis no seu próprio código (como nos exercícios do livro). É o padrão do Python moderno (versão 3.6 ou superior).

#Exemplo: print(f"O resultado é {resultado}")

#2. Use .format() apenas em casos específicos: Quando o texto não está no seu código. Por exemplo:
# Se o texto vier de um arquivo externo ou de uma tradução.
#Se você precisar guardar o "molde" da frase em uma variável para preenchê-la muito depois no código.

#Exemplo: frase_padrao = "Usuário: {} logado." (e depois no código usar frase_padrao.format(nome))

#Resumo para o PyCharm
#No PyCharm, prefira sempre o f-string. Ele ajuda a evitar o erro comum de esquecer a ordem das variáveis (como colocar a pergunta no lugar do nome), já que você escreve o nome da variável exatamente onde ela vai aparecer.