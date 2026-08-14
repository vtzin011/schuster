idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode entrar")
else:
    print("Não pode entrar")

numero = float(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
else:
    print("Número não é positivo")

numero = float(input("Digite outro número: "))

if numero > 0:
    print("Número positivo")
else:
    print("Número negativo ou zero")

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

nota = float(input("Digite a nota (0-10): "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

idade = int(input("Digite a idade: "))

if idade < 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")

temp = float(input("Digite a temperatura em °C: "))

if temp < 15:
    print("Frio")
elif temp <= 25:
    print("Agradável")
else:
    print("Quente")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha a operação (1-4): "))
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

if op == 1:
    print("Resultado:", n1 + n2)
elif op == 2:
    print("Resultado:", n1 - n2)
elif op == 3:
    print("Resultado:", n1 * n2)
elif op == 4:
    if n2 == 0:
        print("Erro: divisão por zero!")
    else:
        print("Resultado:", n1 / n2)
else:
    print("Operação inválida!")

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
c = float(input("Terceiro número: "))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

print("O maior número é:", maior)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

if altura <= 0:
    print("Altura inválida!")
else:
    imc = peso / (altura * altura)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")