#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


void win2(int num) {
    if (num == 0xdeadbeef) {
        printf("You win!\n");
        execve("/bin/sh", NULL, NULL); // This will spawn a shell if called
    } else {
        printf("Try again!\n");
    }
}

void win1() {
    printf("Lab Demo!\n");
    execve("/bin/sh", NULL, NULL); // This will spawn a shell if called
    return;
}

void vuln() {
    char buf[16];
    puts("Enter your name: ");
    gets(buf);
    puts(buf);
    return;
}

int main() {
    vuln();
    return 0;
}
