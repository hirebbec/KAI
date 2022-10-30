#include <stdio.h>
#include <math.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int D = b * b - 4 * a * c;
    if (D > 0) {
        printf("%.4f %.4f", (double)((-b - sqrt((double)D)) / (2 * a)), (double)((-b + sqrt((double)D)) / (2 * a)));
    } else if (D == 0) {
        printf("%.4f", (double)(-b/ (2 * a)));
    } else {
        printf("NO");
    }
    return 0;
}