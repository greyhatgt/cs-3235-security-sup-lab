#include <stdlib.h>
#include <stdio.h>


void win2(int num) {
    if (num == 0xdeadbeef) {
        printf("You win!\n");
    } else {
        printf("Try again!\n");
    }
}

void win1() {
    printf("Lab Demo!\n");
}

int main() {
    char buf[16];
    puts("Enter your name: ");
    gets(buf);
    printf("Hello, %s\n", buf);
    return 0;
}
