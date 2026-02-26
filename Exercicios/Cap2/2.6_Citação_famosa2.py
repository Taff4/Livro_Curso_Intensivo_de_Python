print(f"{'Exe 2.6' :=^50}")

#Repita o Exercício 2.5, porém, desta vez, armazene o nome da pessoa famosa em uma variável chamada famous_person. Em seguida, componha sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua mensagem.

# 1. Definimos as variáveis base (os "ingredientes")
famous_person = 'Hebe de Bonafini'
citacao = 'A única luta que se perde é aquela que se abandona.'

# 2. COMPONDO A MENSAGEM (O segredo do exercício)
# Aqui usamos o 'f' para criar uma NOVA STRING já montada.
# O Python resolve o que está dentro das {chaves} e guarda o texto final na variável 'message'.
message = f'{famous_person} certa vez disse: "{citacao}"'

# 3. EXIBINDO
# Agora não precisamos mais de chaves no print, pois a variável 'message' já é o texto pronto!
print(message)