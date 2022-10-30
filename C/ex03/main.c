#include <stdio.h>

int main() {
    double num1, num2;
    scanf("%lf %lf", &num1, &num2);
    printf("%.10lf", num1 / num2);
    return 0;
}