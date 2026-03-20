"""
Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
para exibir o valor de cada cubo.
"""
# --- EXERCÍCIO: OS DEZ PRIMEIROS CUBOS ---

# 1. Criamos uma lista vazia para armazenar os cubos.
cubos = []

# 2. O range(1, 11) garante que o Python conte de 1 até 10.
# No seu código original, o range(1, 10) parava no 9.
for numero in range(1, 11):
    # 3. Elevamos ao CUBO usando três como expoente (**3).
    # O seu código usou **2, que calcula o quadrado (square).
    cubo = numero ** 3

    # 4. Adicionamos o resultado à nossa lista.
    cubos.append(cubo)

# 5. Utilizamos um laço for para exibir cada valor individualmente, como pede o exercício.
for cubo in cubos:
    print(cubo)