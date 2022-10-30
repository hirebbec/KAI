#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i = 1; i <= num; i++ ) {
        for (int k = num - i; k > 0; k--) {
            printf(" ");
        }
        for (int j = i; j > 0; j--) {
            printf("*");
        }
        printf("\n");
    }
}