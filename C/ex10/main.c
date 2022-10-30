#include <stdio.h>
#include <math.h>

int main() {
    int num;
    scanf("%d", &num);
    int fact = num;
    while (num > 1) {
        num--;
        fact *= num;
    }
    printf("%d", fact);
}