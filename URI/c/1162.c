#include <stdio.h>

int ordena(int vet[], int tam);

void main (void)
{
	int casos, tamTrem;
	int i;

	scanf("%u", &casos);
	while (casos--)
	{
		scanf("%u", &tamTrem);
		int vagoes[tamTrem];
		for (i = 0; i < tamTrem; i++)
			scanf("%d", &vagoes[i]);
		printf("Optimal train swapping takes %u swaps.\n", ordena(vagoes, tamTrem));
	}
}

int ordena(int vet[], int tam)
{
	int i, j, contador = 0, aux;
	while (tam--)
	{
		for (i = 0, j = 1; i < tam; i++, j++)
			if (vet[i] > vet[j])
			{	
				contador++;
				aux = vet[i];
				vet[i] = vet[j];
				vet[j] = aux;
			}
	}
	return contador;
} 