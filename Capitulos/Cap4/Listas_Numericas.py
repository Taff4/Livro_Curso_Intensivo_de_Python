# --- TRABALHANDO COM LISTAS NUMÉRICAS (Curso Intensivo de Python) ---

# 1. Gerando quadrados usando o laço 'for' tradicional
print("--- Quadrados (Método Tradicional) ---")
squares = []
for value in range(1, 11):      # Gera números de 1 a 10
    square = value**2           # Eleva o valor atual ao quadrado
    squares.append(square)      # Adiciona o resultado à lista
print(squares)


# 2. Usando range() para criar listas diretamente
print("\n--- Usando range() e list() ---")
# O range(início, fim) para um número antes do final
numbers = list(range(1, 6))     # Gera [1, 2, 3, 4, 5]
print(f"Lista simples: {numbers}")

# O terceiro argumento do range é o 'passo' (step)
even_numbers = list(range(2, 11, 2)) # Começa no 2, vai até o 10, de 2 em 2
print(f"Números pares: {even_numbers}")


# 3. Estatísticas simples com listas numéricas
print("\n--- Estatísticas ---")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Menor valor: {min(digits)}") # Função min()
print(f"Maior valor: {max(digits)}") # Função max()
print(f"Soma total:  {sum(digits)}") # Função sum()


# 4. List Comprehensions (Abordagem Avançada do Capítulo 4)
# Permite criar a mesma lista de quadrados com apenas uma linha de código
print("\n--- List Comprehension ---")
squares_comp = [value**2 for value in range(1, 11)]
print(squares_comp)


# 5. Demonstração extra do funcionamento do range()
print("\n--- Laço for com range(1, 5) ---")
for value in range(1, 5):
    print(value) # Vai imprimir de 1 a 4