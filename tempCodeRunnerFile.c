#include <stdio.h>

void main()
{
char s[] ("black", "white", "yellow", "violet");

char *ptr[]= (s+3, 8+2, s+1, 8), **p;

p = ptr;

printf("%s\n",--++p+ 3);

}