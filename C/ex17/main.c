#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    while (num % 10 == 0) {
        num /= 10;
    }
    while (num > 0) {
        printf("%d", num % 10);
        num /= 10;
    }
}