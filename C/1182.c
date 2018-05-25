#include <stdio.h>
#include <stdlib.h>

int main(){

	int Coluna, i, j;
	double Matriz[12][12], Resultado=0;
	char Operacao;

	scanf("%d\n", &Coluna);
	scanf("%c\n", &Operacao);

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%lf\n", &Matriz[i][j]);
		}
	}

	for(i=0;i<12;i++){
		Resultado += Matriz[i][Coluna];
	}

	if(Operacao == 'M'){
		Resultado /= 12;
	}

	printf("%.1lf\n", Resultado);

	return 0;
}
