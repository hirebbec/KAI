#include <stdio.h>
#include <math.h>
#include <stdbool.h>


bool check(int num) {
    for (int i = 2; (double)i <= sqrt((double) num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    scanf("%d", &num);
    for (int i = 2; i < num; i++) {
        if (check(i)) {
            printf("%d ", i);
        }
    }
}