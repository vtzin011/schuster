soma = 0

for numero in range(1, 31):
    if numero % 2 != 0:
        soma += numero

print(f"A soma dos números ímpares entre 1 e 30 é: {soma}")

contador = 0

for numero in range(1, 101):
    if numero % 7 == 0 and numero % 2 != 0:
        contador += 1

print(f"A quantidade de números é: {contador}")

maior = None
menor = None

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    
    if maior is None or num > maior:
        maior = num
    
    if menor is None or num < menor:
        menor = num
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")

soma = 0
quantidade_validos = 0

for i in range(8):
    num = float(input(f"Digite o {i+1}º número: "))
    
    if 10 <= num <= 20:
        soma += num
        quantidade_validos += 1

if quantidade_validos > 0:
    media = soma / quantidade_validos
    print(f"A média dos números entre 10 e 20 é: {media:.2f}")
else:
    print("Nenhum número no intervalo entre 10 e 20 foi digitado.")

