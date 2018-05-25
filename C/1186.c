#include <stdio.h>
#include <stdlib.h>

int main(){

	int i, j, c=0, x=0;
	double Matriz[12][12], Resultado=0;
	char Operacao;

	scanf("%c\n", &Operacao);

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%lf\n", &Matriz[i][j]);
		}
	}

	for(i=11;i>=0;i--){
		for(j=1+x;j<12;j++){
			//printf("%d %d\n", i,j);
			Resultado += Matriz[i][j];
			c++;
		}
		x++;
	}

	if(Operacao == 'M'){
		Resultado /= c;
	}

	printf("%.1lf\n", Resultado);

	return 0;
}
