import re
frase = input("Digite uma frase \n")
resultado1 = re.findall(r"[aA]",frase)
qtd = len(resultado1)
if qtd == 0:
    print("Nenhuma letra a encontrada")
else:
    print(f"Existem {qtd} letras A")

telefone = input("Digite um número de telefone \n")
if re.fullmatch(r"\d{5}-\d{4}", telefone):
    print("Telefone válido")
else:
    print("Telefone inválido")

texto = "Python Java HTML CSS"
palavras = re.split(r" ", texto)
print(palavras[0])
print(palavras[1])
print(palavras[2])
print(palavras[3])

senha = input("Digite uma senha \n")
if re.fullmatch(r"\d{6}",senha):
    print("Senha válida ")
else:
    print("Senha inválida ")

texto1 = "banana;maçã;uva;pera"
frutas = re.split(r";", texto1)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

palavra1 = input("victor\n")
if re.match(r"^[Aa]", palavra1):
    print("A frase começa com A")
else:
    print("A frase não começa com A")

texto3 = "10 25 30 45 50"
numeros = re.split(r" ", texto3)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

texto4 = "ana@gmail.com joao@yahoo.com maria@hotmail.com"
email = re.split(r" ", texto4)
print(email[0])
print(email[1])
print(email[2])

frase2 = input("Digite uma frase \n")
frase3 = re.split(r" ", frase2)
if len(frase3) >= 5:
    print(f"Frase longa {len(frase3)} palavras")
else:
    print(f"Frase curta {len(frase3)} palavras")

validos = 0
for i in range (5):
    cpf = input(f"Digite o {i + 1} CPF \n")
    ver1 = re.fullmatch(r'\d{11}', cpf)
    if ver1:
        print("CPF válido")
        validos += 1
    else:
        print("CPF inválido")
print(f"{validos} CPFs foram válidos")
