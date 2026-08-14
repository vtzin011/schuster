for i in range(1, 6):
    idade = int(input(f"Digite a idade {i}: "))
    if idade < 12:
        classificacao="Criança"
    elif idade <= 17:
        classificacao="Adolescente"
    else:
        classificacao="Adulto"

    print(f"Idade {idade}: {classificacao}\n")

positivos = 0
negativos = 0
zeros = 0

for b in range(1, 7):
    numero = float(input(f"Digite o {b}º número: \n"))
    
    if numero > 0:
        positivos += 1
        print("Número positivo")
    elif numero < 0:
        negativos += 1
        print("Número negativo")
    else:
        zeros += 1
        print("Número zero")

print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números zeros: {zeros}")

soma_pares = 0

for c in range(5):
    numero = float(input(f"Número {c+1}: \n"))
    
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos números pares é: {soma_pares}")

soma=0
notav=0
for d in range(1,5):
    nota=float(input(f"Digite a {d}° nota \n"))
    
    if 0 > nota > 10:
        print("Nota inválida")
    else:
        notav+=1
        soma+=nota

media = soma / notav
       
if media >= 7:
    print("Aprovado")
else :
    print("Reprovado")
print(f"e a média é {media}")

contador = 0
contador3 = 0
for e in range(1,8):
    num=float(input("Digite o {e}° número \n"))
    if 10 > num < 20:
        contador += 1
    else:
        contador3 += 1
print(f"{contador} números estavam entre 10 e 20")
print(f"e {contador3} números não estavam entre 10 e 20")

for f in range(1,5):
    senha=input(f"Digite a {f}° senha \n")
    if senha == "1234" or len(senha) <= 6 :
        print("Senha inválida") 
    else:
        print("Senha válida")