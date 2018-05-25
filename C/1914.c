#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define even(x) (x % 2 == 0)

int main(){

	char Nome1[100], Escolha1[5], Nome2[100], Escolha2[5], buf;
	int casos, Num1, Num2, Soma, Result;

	scanf("%d",&casos);

	for(;casos > 0; casos--){

		Soma = 0;
		memset(Nome1, '\0', 100);
		memset(Nome2, '\0', 100);
		memset(Escolha1, '\0', 100);
		memset(Escolha2, '\0', 100);

		scanf("%c", &buf);
		scanf("%s %s %s %s", Nome1, Escolha1, Nome2, Escolha2);
		scanf("%d %d", &Num1, &Num2);
		Soma = Num1 + Num2;
		Result = strcmp(Escolha1, "PAR");
		printf("1 = %s\n2 = %s\n", Nome1, Nome2);

		if(Result != -1 && Result != 1){
			if(even(Soma)){
				printf("\n%s\n", Nome1);
			}else{
				printf("\n%s\n", Nome2);
			}
		}else{
			if(even(Soma)){
				printf("\n%s\n", Nome2);
			}else{
				printf("\n%s\n", Nome1);
			}//internal if
		}//external if
	}
	return 0;
}
