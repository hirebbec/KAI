#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

int main() {
    int size;
    int *m;
    scanf("%d", &size);
    m = malloc(size * sizeof (int));
    for (int i = 0; i < size; i++) {
        scanf("%d", &m[i]);
    }
    int min = m[0];
    for (int i = 0; i < size; i++) {
        if (min > m[i]) {
            min = m[i];
        }
    }
    printf("%d", min);
}