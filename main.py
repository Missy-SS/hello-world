import numpy as np

# 1. Criar uma lista Python simples
lista = [10, 20, 30, 40, 50]

# 2. Converter a lista para um Array NumPy (1D)
array = np.array(lista)

print("Array NumPy:", array)
print("Tipo:", type(array))

# 3. Exemplo de operação rápida (adição em todos os elementos)
array_dobrado = array * 2
print("Array dobrado:", array_dobrado)

# 4. Acessar elementos
print("Primeiro elemento:", array[0])
print(np.average(lista))

valortotal = 0 
for item in lista:
    valortotal = item * item
print(valortotal)

fruits = ["maçã", "banana", "melão"]
for fruit in fruits:
    print(fruit+"teste")
tamanholista = len(fruits) - 1
print(tamanholista)
while tamanholista >= 0:
    print(fruits[tamanholista])
    tamanholista =- 1 

