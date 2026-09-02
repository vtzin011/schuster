#include <stdio.h>

int main() {
    int numeros_fixos[] = {10, 20, 30, 40, 50};
    
    for (int i = 0; i < 5; i++) {
        printf("%d\n", numeros_fixos[i]);
    }
    printf("\n");

    int array_usuario_5[5];
    
    for (int i = 0; i < 5; i++) {
        printf("Digite um numero: ");
        scanf("%d", &array_usuario_5[i]);
    }
    
    printf("[");
    for (int i = 0; i < 5; i++) {
        printf("%d", array_usuario_5[i]);
        if (i < 4) printf(", ");
    }
    printf("]\n\n");

    int numeros[6];
    
    for (int i = 0; i < 6; i++) {
        printf("Digite um numero para o array de 6: ");
        scanf("%d", &numeros[i]);
    }
    
    printf("a) O primeiro elemento: %d\n", numeros[0]);
    printf("b) O terceiro elemento: %d\n", numeros[2]);
    printf("c) O ultimo elemento: %d\n", numeros[5]);
    printf("\n");

    int array_soma[5];
    int soma_total = 0;
    
    for (int i = 0; i < 5; i++) {
        printf("Digite um numero para somar: ");
        scanf("%d", &array_soma[i]);
        soma_total += array_soma[i];
    }
    
    printf("Soma = %d\n", soma_total);
    printf("\n");

    return 0;
}
