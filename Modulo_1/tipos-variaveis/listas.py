# Declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo os elementos 
minha_lista[0] = 'python'
print("minha_lista atualizada:", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) # pega o intervalo da posição 1 até a posição 6
print("minha_lista[:6]:", minha_lista[:6]) # pega da posição 0 até a posição 5
print("minha_lista[2:]:", minha_lista[2:]) # pega a partir da posição 2

# Métodos de lista

# append(): adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# index
indice = minha_lista.index(6)
print("Índice do elemento 6:", indice)

# insert
minha_lista.insert(2, 10)
print("Após o insert(2,10):", minha_lista)

# pop
elemento_removido = minha_lista.pop(6)
print("Elemento removido:", elemento_removido)
print("Após o pop(3):", minha_lista)

# remove
minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# sort (ordem crescente)
minha_lista_numeros = [10, 8, 3, 6, 1]
minha_lista_numeros.sort()
print("Ordenando por sort:", minha_lista_numeros)