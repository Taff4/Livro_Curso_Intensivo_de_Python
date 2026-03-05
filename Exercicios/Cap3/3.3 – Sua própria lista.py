"""
Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma
moto Honda”.
"""
import random

motos = ['Honda', 'Yamaha', 'Mottu']
sorteada = random.choice(motos)
print(sorteada)

motos = ['Honda', 'Yamaha', 'Mottu']
mensagem = 'Gostaria de ter uma moto'

# O random.choice escolhe UM item da lista e entrega para a variável
escolha_1 = random.choice(motos)
print(f"{mensagem} {escolha_1}")

escolha_2 = random.choice(motos)
print(f"{mensagem} {escolha_2}")

escolha_3 = random.choice(motos)
print(f"{mensagem} {escolha_3}")

# Se quiser seguir o livro de forma simples (sem o random):
print(f"Minha primeira moto foi uma {motos[1]}")