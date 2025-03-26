# Estrutura que permite repetir uma ação enquanto uma determinada condição for verdadeira

# for com a lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
    
# for com tupla
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)
    
# for com dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# chaves - keys()
for elemento in pessoa.keys():
    print(elemento)

# valores - values()
for elemento in pessoa.values():
    print(elemento)
    
# chave-valor - items()
for elemento in pessoa.items():
    print(elemento)
# ou
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")