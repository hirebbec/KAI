#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

int *addValue(int *m, int size, int newValue) {
    int *new = malloc((size + 1) * sizeof (int));
    for (int i = 0; i < size; i++) {
        new[i] = m[i];
    }
    new[size] = newValue;
    return new;
}

bool check(int *m, int num, int size) {
    if (num == NULL) {
        return true;
    }
    for (int i = 0; i < size; i++) {
        if (m[i] == num) {
            return false;
        }
    }
    return true;
}

int main() {
    int mSize = 0;
    int num;
    int numSize;
    int *m = NULL;
    scanf("%d", &numSize);
    for (int i = 0; i < numSize; i++) {
        scanf("%d", &num);
        if (check(m, num, mSize)) {
            m = addValue(m, mSize, num);
            mSize++;
        }
    }
    for (int i = 0; i < mSize; i++) {
        printf("%d ", m[i]);
    }
}