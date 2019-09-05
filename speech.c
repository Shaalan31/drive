#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
 
    char data[] = "space,عدين  �  � �";

    char **sentence = (*data);
    
    printf("Old length: %d \n \n",strlen(*sentence));
    /*
    int i;
    for (i=0; i<strlen(sentence);i++)
    {
        if((sentence[i] & 127) == 0 ){
            continue;
        }
        else if((sentence[i] & 0xE0) == 0xE0){
            memmove(&sentence[i], &sentence[i + 3], strlen(sentence) - i);
            //memmove(&sentence[i], &sentence[i + 1], strlen(sentence) - i);
            //memmove(&sentence[i], &sentence[i + 1], strlen(sentence) - i);
            i--;
        }
        else if((sentence[i] & 0xC0) == 0xC0)
        {
            i++;
            continue;
        }
        
    }
    printf("New length: %d \n \n",strlen(sentence));
    
    for (i=0; i<strlen(sentence);i++)
    {
        printf("%d \n",sentence[i]);
    }
    
    */
    
    
    
   /* 
    char* string = u8"ايه الاخبار";

    for (char *s = string; *s; ) {
    printf("<");
    char u[5];
     char *p = u;
     *p++ = *s++;
     if ((*s & 0xC0) == 0x80) *p++ = *s++;
      if ((*s & 0xC0) == 0x80) *p++ = *s++;
      if ((*s & 0xC0) == 0x80) *p++ = *s++;
      *p = 0; 
      
      printf("%x", *u);
      printf(">\n");
}*/
    return 0;
}
/*
void preprocessText(char **data) {
        int sockfd;
        int i;
        for (i=0;i<strlen(*data);i++)
        {
                if(((*data)[i] & 127 ) == 0){
                        continue;
                }
                else if(((*data)[i] & 0xE0) == 0xE0){
                         FILE *before;
                         count = fopen("/home/omar/debug/count.txt","a");
                        fprintf(count, "+1 \n");

                        memmove(&(*data)[i], &(*data)[i+3], strlen(*data) - i);
                        i--;
                }
                else if(((*data)[i] & 0xC0) == 0xC0){
                        i++;
                        continue;
                }
        }
*/