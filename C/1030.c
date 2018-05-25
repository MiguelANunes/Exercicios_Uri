#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct{
    int Cabeca;
    int Cauda;
    int Capacidade;
	int Num_Vivos;
	int *Entradas;
}fila;

fila* criar(int size){

	fila *Criada = malloc(sizeof(fila));
	Criada -> Capacidade = size;
	Criada -> Cabeca = -1;
	Criada -> Cauda = -1;
	Criada -> Num_Vivos = 0;
	Criada -> Entradas = malloc(Criada -> Capacidade * sizeof(int));

	return Criada;
}

bool vazia(fila *F){
	return F -> Cabeca < 0;
}

bool cheia(fila *F){
	if((F -> Cauda + 1) % (F -> Capacidade) == (F -> Cabeca)){
		return true;
	}

	return false;
}

void enqueue(int x, fila *F){
	if (cheia(F)){
		return;
	}
	else{
		F -> Cauda = ((F->Cauda) + 1) % F -> Capacidade;
		F -> Entradas[F->Cauda] = x;
		F -> Num_Vivos++;
		if(F-> Cabeca == -1)
			F-> Cabeca = F -> Cauda;
   }
}

int dequeue(fila *F){
	int Saida;

	if(vazia(F)){
	  return -999;
	}

	else{
		Saida = F->Entradas[F->Cabeca];
		F->Num_Vivos--;
    	if((F->Cabeca) == (F->Cauda)){
    		(F->Cabeca) = (F->Cauda) = -1;
		}
		else{
	    	F->Cabeca = ((F->Cabeca) + 1) % (F->Capacidade);
	    }
      return Saida;
    }
}

void deleta(fila *F){
	if(F){
		if(F->Entradas){
			free(F->Entradas);
		}
		free(F);
	}
}

void exibe(fila *F){
    int i;

    if(vazia(F)){
        printf("-1\n");
	}

	else{
		for(i = F->Cabeca; i != F->Cauda+1; i = (i+1) % F->Capacidade){
			if(F->Entradas[i] != 0)
				printf("%d ", F->Entradas[i]);
		}
		printf("\n");
    }
}

int posVivo(fila *mortos){
	int i=0;

	for(i = mortos->Cabeca; i != mortos->Cauda+1; i = (i+1) % mortos->Capacidade)
		if(mortos->Entradas[i]==1)
			return i;

	return -1;
}

int main(){

	int Casos, i,j;
	int Pessoas, Salto;
	fila *daMorte;

	scanf("%d", &Casos);

	for(j=0;j<Casos;j++){
		scanf("%d %d", &Pessoas, &Salto);
		Salto--;
		daMorte = criar(Pessoas);

		while(!(cheia(daMorte))){
			enqueue(1,daMorte);
		}

		for(i=daMorte->Cabeca; daMorte->Num_Vivos!=1;){

			if(daMorte->Entradas[i] == 1 && daMorte->Entradas[(i+Salto)%daMorte->Capacidade] == 0){
				Salto++;
			}

			if(daMorte->Entradas[i] == 1 && daMorte->Entradas[(i+Salto)%daMorte->Capacidade] == 1){
				daMorte->Entradas[(i+Salto)%daMorte->Capacidade] = 0;
				daMorte->Num_Vivos--;
				i = 1+(i+Salto) == daMorte->Capacidade? 0: 1+(i+Salto)%daMorte->Capacidade;
				continue;
			}
			i=(i+1)%daMorte->Capacidade;
		}
		printf("Case %d: %d\n",j+1, (posVivo(daMorte)+1));

		deleta(daMorte);
	}

	return 0;
}
