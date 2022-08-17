#include<stdio.h>
#include<string.h>

//strcpy() function from string.h already exists, but this is a demonstration of creating a function and using simple pointer arithmetic
//simple demonstration of fundamental skills of using C

void copy(char* dst, char* src){
  while (!(*src == '\0')) {
    *dst = *src;
    src++;
    dst++;
  }
  *dst = '\0';
}
int main(){
  char srcString[] = "We promptly judged antique ivory buckles for the next prize!";
  char dstString[strlen(srcString) + 1];
  copy(dstString, srcString);
  printf("%s", dstString);
}
