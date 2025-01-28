nome = "Pedro"
sobrenome = "Souza"

nome_completo = "Pedro Souza"

print(nome)
print("Método upper:",nome.upper())
print("Método lower:",nome.lower())

print("Método count:", nome_completo.count("o"))
print("Método find:", nome_completo.find("o")) #acha a posição da primeira letra "o" que aparece

print("Método encode:", nome_completo.encode()) #conversão em bytes
print("Método decode:", nome_completo.encode().decode()) #decodificando os bytes

print("Método replace:", nome_completo.replace("d", "r")) #substitui a primeira letra pela segunda letra
print("Método replace:", nome_completo.replace("d", "r").replace("o", "e")) #mais de uma substituição e assim por diante...

print("Método join:", "-".join(nome_completo)) #separando por traços
print("Método split:", nome_completo.split(" ")) #separa em lista

nome_com_ruido = "xPedro Souzax"
print("Método strip:", nome_com_ruido.strip("x")) #elimina caracteres das extremidades
print("Método strip da direta:", nome_com_ruido.rstrip("x")) #elimina caracteres da extremidade direita

# Comparadores
print("Comparador start with:", nome_completo.startswith("Pe")) #começa com "Pe"
print("Comparador in:", "dro" in nome_completo) #checa se "dro" está presente em nome_completo e retorna true se estiver e false para se não estiver
print("Comparador not in:", "dro" not in nome_completo) #checa se "dro" não está presente em nome_completo e retorna true se não estiver e false para se estiver
