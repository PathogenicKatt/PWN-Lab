#include <string.h>
#include <stdio.h>

void vuln_func()
{
    char buffer[64];
    printf("Enter your name: ");
    gets(buffer); // Vulnerable function
    printf("Hello: %s\n", buffer);
}

void print_flag()
{
    printf("Congratulations! You've triggered the flag function!\n");
    exit(0);
}

int main()
{
    vuln_func();
    return 0;
}