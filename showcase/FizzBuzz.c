#include <stdio.h>

int main() {

printf("The goal of FizzBuzz is to output numbers 1-100. For multiples of 3, output \"Fizz\". For multiples of 5, output \"Buzz\". For multiples of 3 and 5, output \"FizzBuzz.\"\n\n");
//for initialize variable
int i = 1;
//for FizzBuzz
for (;i < 101;i++) {
if (!(i % 3 == 0 ) && !(i % 5 == 0)) {
  printf("%d\n", i);
}
else if ((i % 3 == 0) && (i % 5 == 0)) {
  printf("FizzBuzz\n");
}
else if ((i % 3 == 0) && !(i % 5 == 0)) {
  printf("Fizz\n");
}
else if ((i % 5 == 0) && !(i % 3 == 0)) {
printf("Buzz\n");
}
}
}

