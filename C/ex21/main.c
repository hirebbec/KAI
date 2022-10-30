#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
    double m[150];
    for (int i = 0; i < 150; i++) {
        scanf("%lf", &m[i]);
    }
    double min = m[0], max = m[0], sum = 0.0;
    for (int i = 0; i < 150; i++) {
        sum += m[i];
        if (max < m[i]) {
            max = m[i];
        }
        if (min > m[i]) {
            min = m[i];
        }
    }
    printf("%.4lf %.4lf %.4lf", max, min, sum / 150.0);
}