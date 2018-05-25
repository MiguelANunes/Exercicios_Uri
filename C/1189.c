#include <stdio.h>
#include <stdlib.h>

int main(){

	int i, j, c=0, y=10;
	double Matriz[12][12], Resultado=0;
	char Operacao;

	scanf("%c\n", &Operacao);

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%lf\n", &Matriz[i][j]);
		}
	}

	for(i=1;i<11;i++){
		if(i==6){
			y = 6;
		}
		for(j=0;j<=10-y;j++){
			if(i == j){
				break;
			}
			printf("%d %d\n", i,j);
			Resultado += Matriz[i][j];
			c++;
		}
		if(i>=6){
			y++;
		}else{
			y--;
		}
	}


	if(Operacao == 'M'){
		Resultado /= c;
	}

	printf("%.1lf\n", Resultado);

	return 0;
}
