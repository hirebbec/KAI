#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>

bool check(char c, char *str, int len) {
    if (str == NULL)
        return true;
    int i = 0;
    while (i < len) {
        if (((str[i] >= 'a' && str[i] < 'z') || (str[i] >= 'A' && str[i] < 'Z')) && (str[i] == c || str[i] == c + 32 || str[i] == c - 32))
            return false;
        i++;
    }
    return true;
}

char *addChar(char c, char *str, int len) {
    char *new = malloc(len + 1);
    for (int i = 0; i < len; i++) {
        new[i] = str[i];
    }
    new[len] = c;
    return new;
}

int main() {
    int size;
    int len = 0;
    scanf("%d\n", &size);
    char *str = malloc(size + 1);
    for (int i = 0; i < size; i++){
       str[i]=(char)fgetc(stdin);
    }
    read (0, NULL, 1);
    char *uniq = NULL;
    for (int i = 0; i < size; i++) {
        if (check(str[i], uniq, len)) {
            uniq = addChar(str[i], uniq, len);
            len++;
        }
    }
    for (int i = 0; i < len; i++) {
        printf("%c", uniq[i]);
    }
    printf("\n");
}