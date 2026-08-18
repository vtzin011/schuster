#include <stdio.h>
#include <stdlib.h>

int main() {
    // Variáveis para os exercícios
    char nome[100], cidade[100];
    int idade, n1_int, n2_int, num, qtd, horas;
    float n1_float, n2_float, nota1, nota2, nota3, media;
    float base, altura_ret, preco, salario, bonus;

    printf("=== EXERCICIO 1 e 13: Dados Pessoais e Boas-Vindas ===\n");
    printf("Digite seu nome: ");
    scanf(" %[^\n]", nome);
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("Digite sua altura (ex: 1.75): ");
    scanf("%f", &altura_ret); // Usando temporariamente para ler altura do aluno
    printf("Digite sua cidade: ");
    scanf(" %[^\n]", cidade);
    
    printf("\nSeja muito bem-vindo, %s!\n", nome);
    printf("\n--- Informacoes do Aluno ---\n");
    printf("Nome: %s\n", nome);
    printf("Idade: %d anos\n", idade);
    printf("Altura: %.2f m\n", altura_ret);
    printf("Cidade: %s\n", cidade);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 2: Idade Informada ===\n");
    printf("A idade informada anteriormente foi: %d anos.\n", idade);
    printf("===================================================\n\n");

    printf("=== EXERCICIOS 3, 4, 5, 8 e 9: Operacoes com Inteiros ===\n");
    printf("Digite o primeiro numero inteiro (n1): ");
    scanf("%d", &n1_int);
    printf("Digite o segundo numero inteiro (n2): ");
    scanf("%d", &n2_int);
    
    // Exercícios 3, 4 e 5
    printf("Soma (n1 + n2): %d\n", n1_int + n2_int);
    printf("Subtracao (n1 - n2): %d\n", n1_int - n2_int);
    printf("Multiplicacao (n1 * n2): %d\n", n1_int * n2_int);
    
    // Exercício 8 e 9 (usando o primeiro número como base)
    printf("Dobro de n1: %d\n", n1_int * 2);
    printf("Triplo de n1: %d\n", n1_int * 3);
    printf("Antecessor de n1: %d\n", n1_int - 1);
    printf("Sucessor de n1: %d\n", n1_int + 1);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 6: Media de Tres Notas ===\n");
    printf("Digite as tres notas do aluno separadas por espaco: ");
    scanf("%f %f %f", &nota1, &nota2, &nota3);
    media = (nota1 + nota2 + nota3) / 3.0;
    printf("Media aritmetica: %.2f\n", media);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 7: Area de um Retangulo ===\n");
    printf("Digite a base do retangulo: ");
    scanf("%f", &base);
    printf("Digite a altura do retangulo: ");
    scanf("%f", &altura_ret);
    printf("Area do retangulo: %.2f\n", base * altura_ret);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 10: Valor Total da Compra ===\n");
    printf("Digite o preco do produto: ");
    scanf("%f", &preco);
    printf("Digite a quantidade comprada: ");
    scanf("%d", &qtd);
    printf("Valor total da compra: R$ %.2f\n", preco * qtd);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 11: Salario Final ===\n");
    printf("Digite o salario do funcionario: ");
    scanf("%f", &salario);
    printf("Digite o valor do bonus: ");
    scanf("%f", &bonus);
    printf("Salario final: R$ %.2f\n", salario + bonus);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 12: Conversao de Horas ===\n");
    printf("Digite a quantidade de horas: ");
    scanf("%d", &horas);
    printf("%d horas correspondem a %d minutos.\n", horas, horas * 60);
    printf("===================================================\n\n");

    printf("=== EXERCICIO 14: Menu Completo de Operacoes (Reais) ===\n");
    printf("Digite o primeiro numero real: ");
    scanf("%f", &n1_float);
    printf("Digite o segundo numero real: ");
    scanf("%f", &n2_float);
    
    printf("Soma: %.2f\n", n1_float + n2_float);
    printf("Subtracao: %.2f\n", n1_float - n2_float);
    printf("Multiplicacao: %.2f\n", n1_float * n2_float);
    if (n2_float != 0) {
        printf("Divisao: %.2f\n", n1_float / n2_float);
    } else {
        printf("Divisao: Erro! Nao e possivel dividir por zero.\n");
    }
    printf("===================================================\n");

    return 0;
}
