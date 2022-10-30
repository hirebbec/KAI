#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int i;
        int n;
        char *str;
        char c;

        scanf("%d\n", &n);
        str = (char*)malloc(sizeof(char)*n);

        for (i=0; i<n; i++){

           str[i]=(char)fgetc(stdin);

        }
        read (0, &c, 1);
        i = 0;
        while (str[i]) {
        if (str[i] >= 'a' && str[i] < 'z') {
            str[i] = str[i] - 32;
        }
        i++;
    }

        write(1, str, n);
        write(1, "\n", 1);

        return 0;
}