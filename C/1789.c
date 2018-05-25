#include <stdio.h>
#include <stdlib.h>

int index_max_value(int* vetor, int size_vetor);

int main(){

	int Num_Lesmas, *Vel_Lesmas, Pos_veloz, i;

	while(scanf("%d",&Num_Lesmas) != EOF){
		Vel_Lesmas = malloc(Num_Lesmas*sizeof(int));

		for(i = 0; i < Num_Lesmas; i++)
			scanf("%d",&Vel_Lesmas[i]);

		Pos_veloz = index_max_value(Vel_Lesmas,Num_Lesmas);

		if(Vel_Lesmas[Pos_veloz] < 10){
			printf("1\n");
		}else if(Vel_Lesmas[Pos_veloz] >= 10 && Vel_Lesmas[Pos_veloz] < 20){
			printf("2\n");
		}else if(Vel_Lesmas[Pos_veloz] >= 20){
			printf("3\n");
		}
	}//while EOF
	
	return 0;
}

int index_max_value(int* vetor, int size_vetor){
	int i = 0, maior = -1;

	for(; i < size_vetor; i++){
		if(vetor[i] >= maior)
			maior = i;
	}

	return maior;

}