#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i = 1; i <= num; i++ ) {
        for (int j = i; j > 0; j--) {
            printf("*");
        }
        printf("\n");
    }
}