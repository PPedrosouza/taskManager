# imutáveis

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4, 3) 
print("Minha tupla:", minha_tupla)

print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[-1]:", minha_tupla[-1])

# Métodos

# count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem, "vezes")

# index
indice = minha_tupla.index(3)
print("Índice da primeira ocorrência do elemento 3:", indice)

# exercícios

# concatenação de tuplas       
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)


# desempacotamento de tuplas
tupla = ("Python", "é", "incrível")
a, b, c = tupla
print(a)
print(b)
print(c)

