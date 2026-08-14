def menu():
    print("\n--- MENU DE QUESTÕES ---")
    print("4. Positivo, Negativo ou Zero")
    print("5. Condição de Desconto")
    print("6. Comparação A e B")
    print("7. Pares de 1 a 10")
    print("8. Soma de 1 a 5")
    print("9. Números > 5 (0 a 10)")
    print("10. Análise Completa de Número")
    print("0. Sair")
    return input("\nEscolha uma questão para executar: ")

while True:
    opcao = menu()

    if opcao == '4':
        n = float(input("Digite um número: "))
        if n > 0: print("Positivo")
        elif n < 0: print("Negativo")
        else: print("Zero")

    elif opcao == '5':
        idade = int(input("Idade: "))
        estudante = input("Estudante (s/n): ").lower()
        if idade < 18 or estudante == 's':
            print("Com desconto")
        else:
            print("Sem desconto")

    elif opcao == '6':
        # Completando o código da questão 6
        a = int(input("A: "))
        b = int(input("B: "))
        if a > b: print('A é maior')
        elif a < b: print('B é maior')
        else: print('São iguais')

    elif opcao == '7':
        print("Pares de 1 a 10:")
        for i in range(1, 11):
            if i % 2 == 0: print(i, end=" ")
        print()

    elif opcao == '8':
        soma = sum(range(1, 6))
        print(f"A soma de 1 a 5 é: {soma}")

    elif opcao == '9':
        print("Números de 0 a 10 maiores que 5:")
        for i in range(11):
            if i > 5: print(i, end=" ")
        print()

    elif opcao == '10':
        num = int(input("Digite um número: "))
        res = "Positivo" if num > 0 else "Negativo" if num < 0 else "Zero"
        paridade = "Par" if num % 2 == 0 else "Ímpar"
        print(f"O número {num} é {res} e {paridade}.")

    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

