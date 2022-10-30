#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            printf("%d", i);
            for (int j = 2; j <= i / 2; j++) {
                if (i % j == 0) {
                    printf(" %d", j);
                }
            }
            printf("\n");
        }
    }
}