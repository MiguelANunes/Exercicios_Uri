#include <stdio.h>
#include <stdlib.h>

int main(){

	int Linha, i, j;
	double Matriz[12][12], Resultado=0;
	char Operacao;

	scanf("%d\n", &Linha);
	scanf("%c\n", &Operacao);
	//printf("%d\n", Linha);

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%lf\n", &Matriz[i][j]);
		}
	}

	for(i=0;i<12;i++){
		Resultado += Matriz[Linha][i];
	}

	if(Operacao == 'M'){
		Resultado /= 12;
	}

	printf("%.1lf\n", Resultado);

	return 0;
}
