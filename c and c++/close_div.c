#include <stdio.h>
#include <string.h>
void main(int argc, char *argv[]){
    char *isdiv = "<div>";
    char *test2 = "<div>ndjd<div>nhh";
    // char *test1 = "<p><<div><divm>hello<p><div>";
    char *test1 = "<div><p>hi<p><div>l<div><P><P><div>";
    
    char tmp[6];
    char *closingDiv = "<\\div>";
    int i, rc = 0;
    int iteration = 0;
    char result[50];

    printf("%d\n", strcmp(isdiv,"<div>"));
    printf("%d\n", 2 == 2);
    printf("%d\n", 0 % 2 == 0);
    while(1){
        if(test1[i] == '\0'){
            result[rc] = '\0';
            break;
        }
        // printf("%c\n", test1[i]);
        
        //begining thougths
        /*if(test1[i] == '<'){
            for(int j =0; j<=4;j++){
                tmp[j] = test1[i +j];
            }
            if(strcmp(isdiv,tmp) == 0){
                iteration++;
                if(iteration % 2 == 0){
                    test1[]
                }
            }
        }*/
        if(test1[i] == '<'){
            for (int j = 0; j < 5; j++) {  // Fix indexing
                tmp[j] = test1[i + j]; 
            }
            tmp[5] = '\0';
            if(strcmp(isdiv,tmp) == 0){
                iteration++;
                printf("found\n");
                if(iteration % 2 == 0){
                    for(int k =0; k < 6; k++){
                        // if(k == 1){
                        //     result[1] = '\\';
                        //     i++;
                        // }
                        result[rc + k] = closingDiv[k]; //3
                    }
                    // int l = 0;
                    // while (1)
                    // {
                    //     if(result[l] == '\0'){
                    //         break;
                    //     }
                    //     printf("%c",result[l]);
                    //     l++;
                    // }
                    rc += 6; 
                    i += 5;
                    continue;
                }
            }
        }
        result[rc] = test1[i];
        i++;
        rc++;
    }
    // int l = 0;
    // while (1)
    // {
    //     if(result[l] == '\0'){
    //         break;
    //     }
    //     printf("%c",result[l]);
    //     l++;
    // }
    printf("Modified string: %s\n", result); 
    
}