#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

int main() {
    int **m;
    int lines;
    int *digitsInLines;
    scanf("%d", &lines);
    m = malloc(lines * sizeof (int *));
    digitsInLines = malloc(lines * sizeof (int));
    for (int i = 0; i < lines; i++) {
        scanf("%d", &digitsInLines[i]);
        m[i] = malloc(digitsInLines[i] * sizeof (int));
        for (int j = 0; j < digitsInLines[i]; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    for (int i = 0; i < lines; i++) {
        int min = m[i][0];
        for (int j = 0; j < digitsInLines[i]; j++) {
            if (min > m[i][j]) {
                min = m[i][j];
            }
        }
        if (i == lines - 1) {
            printf("%d", min);
        } else {
            printf("%d ", min);
        }
    }
}