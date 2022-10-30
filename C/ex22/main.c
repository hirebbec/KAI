#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool check(int num) {
    for (int i = 2; (double)i <= sqrt((double)num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int m[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &m[i]);
    }
    for (int i = 0; i < 10; i++) {
        if (check(m[i])) {
            printf("%d ", m[i]);
        }
    }
}