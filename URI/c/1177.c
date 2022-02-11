#include <stdio.h>

int main(void)
{
  int vetor[1000];
  int i, valor;
  int cont = 0;

  scanf("%d", &valor);
  for (i=0; i<1000; i++)
  {
    vetor[i] = cont;
    cont++;
    if (cont == valor)
    {
      cont = 0;
    }
    printf("N[%d] = %d\n", i, vetor[i]);
  }
  return 0;
}