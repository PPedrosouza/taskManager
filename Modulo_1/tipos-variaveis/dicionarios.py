# coleção n ordenanda de pares chave - valor

# criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade" : "São Paulo"}
print("Meu dicionário de exemplo:", pessoa)

# acessando valores por chave
print("Nome:", pessoa['nome'])
pessoa['sobrenome'] = "Silva"
print("Sobrenome:", pessoa['sobrenome'])
print("Idade:", pessoa['idade'])
print("Cidade:", pessoa['cidade'])

pessoa['sobrenome'] = 'Silva'
print("Sobrenome:", pessoa['sobrenome'])

pessoa['idade'] = 31
print("Idade atualizada:", pessoa['idade'])

# removendo um par chave-valor
del pessoa['sobrenome']
print(pessoa)

# métodos: keys(), values(), items()
chaves = pessoa.keys()
# print("Chaves do dicioário:", chaves)
# print("Primeira chave:", chaves[0])

chaves = list(pessoa.keys())
print("Chaves do dicioário:", chaves)
print("Primeira chave do dicionário:", chaves[0])

valores = list(pessoa.values())
print("Valores do dicioário:", valores)
print("Primeira valor do dicionário:", valores[0])

items = list(pessoa.items())
print("Pares chave-valor do dicionário:", items)
print("Primeira chave-valor: %s = %s" % (items[0][0], items[0][1]))
