#include <stdio.h>

int concat( char *first, char *last);

int main(void){
    char first[20] = "peterson";
    char *last = "kinyanjui";
    concat(first, last);
    return 0;
}
int concat(char *first, char *last){
    int index = 0;
    // printf("%p", first);
    while(1){
        if(first[index] == '\0'){
        break;
    }
    index++;
    // printf("letter: %c", *(first +1));
    }
    printf("%d", index);
    int last_index = 0;
    while (1)
    {
        if(last[last_index] == '\0'){
            break;

        }
        first[index] = last[last_index];
        last_index++;
        index++;
    }
    
    printf("%s", first);
}