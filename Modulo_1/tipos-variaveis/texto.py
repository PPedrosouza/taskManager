# declaração
nome_completo = "Pedro Souza"

nome_completo_com_aspas = """Pedro
Souza"""

nome_completo_quebra = "Pedro \
Souza"

nome = "Pedro"
sobrenome = "Souza"

# print(nome_completo)
# print(nome_completo_com_aspas)
# print(nome_completo_quebra)
# print(nome)
# print(sobrenome)

# formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Pedro" + "Souza") 
print("Nome completo (4a forma):" + "Pedro" , "Souza")
print("Nome completo (5a forma):", nome_completo_com_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))