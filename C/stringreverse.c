#include <stdio.h>
#include <string.h>

char* REVERSE(char str[]) {
  int len = strlen(str);
  char reversed[len + 1]; 
  int i;

  for (i = 0; i < len; i++) {
    reversed[i] = str[len - i - 1];
  }

  reversed[len] = '\0';
}

int main() {
  char inputString[100];

  printf("Enter a string: ");
  scanf("%s", inputString);

  char *reversedString = REVERSE(inputString);
  printf("Reversed string: %s\n", reversedString);

  return 0;
}