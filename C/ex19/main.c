#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
    int m[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &m[i]);
    }
    int min = m[0], max = m[0];
    for (int i = 0; i < 10; i++) {
        if (max < m[i]) {
            max = m[i];
        }
        if (min > m[i]) {
            min = m[i];
        }
    }
    printf("%.4lf", (double)((max + min) / 2));
}