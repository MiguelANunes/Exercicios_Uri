#include <stdio.h>
#include <stdlib.h>

int main(){

	int i, j, c=0;
	double Matriz[12][12], Resultado=0;
	char Operacao;

	//scanf("%d\n", &Coluna);
	scanf("%c\n", &Operacao);

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%lf\n", &Matriz[i][j]);
		}
	}

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			if(j<=i){
				continue;
			}else{
				Resultado += Matriz[i][j];
				c++;
			}
		}
	}

	if(Operacao == 'M'){
		Resultado /= c;
	}

	printf("%.1lf\n", Resultado);

	return 0;
}
