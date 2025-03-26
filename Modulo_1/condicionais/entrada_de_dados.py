# if, elif e else

# exemplo de "if"
idade = int(input("Quantos anos você tem?"))
print("Exemplo de comando if")

if idade > 18:
    print("Você é maior de idade e tem mais de 18 anos.")
    
if idade >= 18:
    print("Você é maior de idade.")
    
if idade < 18:
    print("Você é menor de idade") 
    
if idade == 19:
    print("Você é maior de idade e tem 19 anos.")
    
if idade != 10:
    print("Você não tem 10 anos") 
    

# Exemplo de "else"
idade = 19
print("Exemplo de comando else")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")
    
# Exemplo de "elif"
idade = 19
print("Exemplo de comando elif")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade")
    

# Exemplo de condição em uma única linha
mensagem = "Pode tirar a carteira de habilitação" if idade >=18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)