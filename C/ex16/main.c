#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    int max = num % 10;
    while (num > 0) {
        if (max < num % 10) {
            max = num % 10;
        }
        num /= 10;
    }
    printf("%d", max);
}