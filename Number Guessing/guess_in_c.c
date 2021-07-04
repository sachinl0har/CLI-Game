#include <stdio.h>

int main(){
    system("cls");
    int num, guess, myNum, tries;
    int MAXTRY = 5;
    num = rand() % 10 + 1;
    printf("Guess My Number Game\n\n");
    guess = 0;
    tries = 0;
    do{
        if(tries == 5){
            printf("Last Chance! Think Hard.\n");
        }
        printf("Enter Your Guess: \n");
        scanf("%d", &myNum);
        tries++;
        if(myNum > num){
            printf("Too High!\n\n");
        }else if(myNum < num){
            printf("Too Low!\n\n");
        }else{
            printf("\nCorrect! You Got it in %d Guesses!\n", tries);
        }
    }while((guess == 0) && (tries <= MAXTRY));
    return 0;
}
