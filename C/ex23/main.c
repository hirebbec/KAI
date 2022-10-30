#include <stdio.h>
#include <math.h>
#include <stdbool.h>
int main() {
    int m[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &m[i]);
    }
    bool flag = true;
    while (flag) {
        flag = false;
        for (int i = 0; i < 9; i++) {
            if (m[i] > m[i + 1]) {
                int tmp = m[i];
                m[i] = m[i + 1];
                m[i + 1] = tmp;
                flag = true;
            }
        }
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", m[i]);
    }
}