import re

texto = "kewyn tem 15 anos e Pedro 18"
numeros = re.findall(r'\d+', texto)
print(numeros)

frase = input("Digite uma frase \n")
ver = re.search(r'\d', frase)
if ver:
    print("Existe número")
else:
    print("Não tem número")

cpf = input("Digite um CPF \n")
ver1 = re.fullmatch(r'\d{11}', cpf)
if ver1:
    print("CPF válido")
else:
    print("CPF inválido")

texto = "Kewyn,Pedro,Nicolas,Adryele"
nomes = re.split(r",", texto)

for nome in nomes:
    print(nome)


texto = "Programação em Python"
vogais = re.findall(r"[aeiouAEIOUáàãâéêíóôõúü]", texto)

print("Vogais:", vogais)
print("Quantidade:", len(vogais))

telefone = input("Digite o telefone \n")

if re.fullmatch(r"\d{5}-\d{4}", telefone):
    print("Telefone válido")
else:
    print("Telefone inválido")

texto = "casa bola sol gato mesa"
palavras_4_letras = re.findall(r"\b[A-Za-z]{4}\b", texto)

print("Palavras com 4 letras:", palavras_4_letras)

texto = "Contato: joao@gmail.com"
email = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", texto)
if email:
    print("Email encontrado:", email.group())

email = input("Digite o email escolar: ")
padrao = r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@escola\.pr\.gov\.br$"
if re.fullmatch(padrao, email):
    print("Email válido")
else:
    print("Email inválido")

texto = "10-20-30-40"
numeros = re.split(r"-", texto)

print("Lista completa:", numeros)
print("Quantidade de números:", len(numeros))

texto = "#python é usado em #dados e #ia"
hashtags = re.findall(r"#\w+", texto)

print("Hashtags encontradas:", hashtags)
data = input("Digite a data (dd/mm/aaaa): ")

if re.fullmatch(r"\d{2}/\d{2}/\d{4}", data):
    print("Data válida")
else:
    print("Data inválida")

senha = input("Digite uma senha de 6 números: ")

if re.fullmatch(r"\d{6}", senha):
    print("Senha válida")
else:
    print("Senha inválida")

texto = "JOAO foi aprovado com MARIA"
palavras_maiusculas = re.findall(r"\b[A-Z]+\b", texto)

print("Palavras maiúsculas:", palavras_maiusculas)
print("Quantidade encontrada:", len(palavras_maiusculas))

texto = "Python;Java,C++,JavaScript"
linguagens = re.split(r"[;,]", texto)

print("Linguagens:", linguagens)

frase = input("Digite uma frase: ")

if re.match(r"^Python", frase):
    print("A frase começa com Python")
else:
    print("A frase não começa com Python")

texto = "10 15 22 31 48 57"
pares = re.findall(r"\b\d*[02468]\b", texto)

print("Números pares encontrados:", pares)

nome = input("Digite seu nome (ex: nome.sobrenome): ")
email = input("Digite o email: ")
padrao_email = r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@escola\.pr\.gov\.br$"
if re.fullmatch(padrao_email, email):
    print("Cadastro aprovado")
else:
    print("Cadastro recusado")

texto = "Lucas tirou 8, Maria tirou 10 e João tirou 7"
notas_str = re.findall(r"\d+", texto)

notas = [int(n) for n in notas_str]
media = sum(notas) / len(notas)
if media >= 7:
    print(f"Média: {media:.1f} - Turma aprovada")
else:
    print(f"Média: {media:.1f} - Turma reprovada")