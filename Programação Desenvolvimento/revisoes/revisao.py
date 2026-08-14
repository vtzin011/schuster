nome = "Victor"
idade = 17
print(f"Nome: {nome}, Idade: {idade}")
a = 10
b = 20
soma = a + b
print(f"A soma de {a} + {b} é: {soma}")
numero1 = 50
numero2 = 15
subtracao = numero1 - numero2
print(f"O resultado da subtração é: {subtracao}")
nota1 = 8.5
nota2 = 7.0
media = (nota1 + nota2) / 2
print(f"A média das notas é: {media}")
ano_nascimento = 1998
ano_atual = 2024
idade_calculada = ano_atual - ano_nascimento
print(f"A idade da pessoa é: {idade_calculada} anos")
preco = 29.90
quantidade = 3
total = preco * quantidade
print(f"O valor total da compra é: R$ {total:.2f}")
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura * altura
print(f"A área do retângulo é: {area}")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
if operacao == '+':
    print(f"Resultado: {num1 + num2}")
elif operacao == '-':
    print(f"Resultado: {num1 - num2}")
elif operacao == '*':
    print(f"Resultado: {num1 * num2}")
elif operacao == '/':
    print(f"Resultado: {num1 / num2}")
else:
    print("Operação inválida.")
