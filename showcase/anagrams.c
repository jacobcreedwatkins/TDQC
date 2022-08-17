#include <stdio.h>
#include <string.h>


/* simple program to determine whether or not two strings are anagrams. 
to do: have the program take two user-inputted strings and determine if they are anagrams or not.
not really practical, more of a demonstration on iterating through arrays and using basic loops */

int main() {
int counter1[] = {0, 0, 0, 0};
int counter2[] = {0, 0, 0, 0};
char s1[] = "dbb cccccaacb cdbababdcdcdab dcdad";
char s2[] = "bbbcc bdddccccad cdbbaaacaccdabdd";


//for iterating through string 1 and counting occurences
for (int i = 0; i < strlen(s1); i++) {
  if (s1[i] == 'a') {
    counter1[0]++;}
  if (s1[i] == 'b') {
    counter1[1]++;}
  if (s1[i] == 'c') {
    counter1[2]++;}
  if (s1[i] == 'd') {
    counter1[3]++;}
  if (s1[i] == ' ') {
    continue;}
}
//for iterating through string 2 and counting occurences
for (int j = 0; j < strlen(s1); j++) {
  if (s2[j] == 'a') {
    counter2[0]++;}
  if (s2[j] == 'b') {
    counter2[1]++;}
  if (s2[j] == 'c') {
    counter2[2]++;}
  if (s2[j] == 'd') {
    counter2[3]++;}
  if (s2[j] == ' ') {
    continue;}
}

//for setting mismatch flag
int flag = 0;
for (int x = 0; x < 3; x++){
  if (!(counter1[x] == counter2[x])) {
  flag = 1;}
if (counter1[x] == counter2[x]) {
  flag = 0;}
}
if (flag == 0) {
  printf("Anagram!\n");}
else {
  printf("Not Anagram!\n");
}
}
