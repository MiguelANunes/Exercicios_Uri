#include <stdio.h>
#include <stdlib.h>
#define even(x) (x % 2 == 0)

int main(){

	int S, casos;
	scanf("%d", &casos);
	for(;casos > 0; casos--){
		scanf("%d", &S);
		if(even(S))
			printf("0\n");
		else
			printf("1\n");
	}
	return 0;
}
