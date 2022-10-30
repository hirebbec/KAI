#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
    int m[4][4];

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (j == 3) {
                printf("%d", m[j][i]);
            } else {
                printf("%d ", m[j][i]);
            }
        }
        printf("\n");
    }
}