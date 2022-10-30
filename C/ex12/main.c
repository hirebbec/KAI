#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i = num; i > 0; i-- ) {
        for (int j = num; j > 0; j--) {
            printf("*");
        }
        printf("\n");
    }
}