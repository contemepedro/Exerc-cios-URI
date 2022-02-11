#include <stdio.h>

int main(void)
{
  int vetor[10];
  int valor, i;

  scanf("%d", &valor);
  vetor[0] = valor;
  printf("N[0] = %d\n", valor);
  for (i=1; i<10; i++)
  {
    vetor[i] = vetor[i-1]*2;
    printf("N[%d] = %d\n", i, vetor[i]);
  }
  return 0;
}