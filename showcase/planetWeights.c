int main() {

//for explain scenario
printf("Greetings, interplanetary fighter! In preparation for your upcoming fight, we must calculate your weight for the planet you will be fighting on.\nThe order of the planets starts from nearest the sun going outward, Mercury being 1 and ending with Neptune at 7.\nRemember the mnemonic, \"My Very Educated Mother Just Served Us Noodles.\"\n\n\n\n");

//for ask weight
float earthWgt, newWgt;
int planet;
printf("Enter your weight on Earth: ");
scanf("%f", &earthWgt);
//for ask planet
printf("Enter a number for the planet you want to fight on: ");
scanf("%d", &planet);

switch(planet) {
  case 1:
  newWgt = earthWgt * .38;
  printf("Your weight on Mercury is %f pounds.\n", newWgt);
  break;
  case 2:
  newWgt = earthWgt * .91;
  printf("Your weight on Venus is %f pounds.\n", newWgt);
  break;
  case 3:
  newWgt = earthWgt * .38;
  printf("Your weight on Mars is %f pounds.\n", newWgt);
  break;
  case 4:
  newWgt = earthWgt * 2.34;
  printf("Your weight on Jupiter is %f pounds.\n", newWgt);
  break;
  case 5:
  newWgt = earthWgt * 1.06;
  printf("Your weight on Saturn is %f pounds.\n", newWgt);
  break;
  case 6:
  newWgt = earthWgt * .92;
  printf("Your weight on Uranus is %f pounds.\n", newWgt);
  break;
  case 7:
  newWgt = earthWgt * 1.19;
  printf("Your weight on Neptune is %f pounds.\n", newWgt);
  break;
  default:
  printf("Invalid planet number. Please pick a number between 1 and 7!\n");
}
