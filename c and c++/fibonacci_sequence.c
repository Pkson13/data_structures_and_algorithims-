#include <stdio.h>
#include <stdlib.h>

void main(int argc, char *argv[]){
    // a number that is the sum of the last to numbers starting from 0
    printf("%d\n", argc);
    if (argc < 2){
        printf("Usage: %s <max_number>\n", argv[0]);
        exit(99);
    }
    for (int i =0;i <argc; i++){
        printf("%s\n", argv[i]);
    }
    printf("test : %s", argv[1]);

    int max = atoi(argv[1]);
    int x = 0,y = 1, z;
    printf("%d\n", x);
    printf("%d\n", y);
    while (1){
        z = x + y;
        if (z >= max){
            break;
        }
        printf("%d\n", z);
        x =y;
        y =z;
    }
}