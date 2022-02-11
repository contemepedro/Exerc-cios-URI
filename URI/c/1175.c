#include <stdio.h>

int main(void)
{
  int vetor[20], vetor2[20];
  int valor;
  int i = 0;
  int j = 19;

  for(i=0; i<20; i++)
  {
    scanf("%d", &valor);
    vetor[i] = valor;
  }
  for (i=0; i<20; i++)
  {
    vetor2[i] = vetor[j];
    j--;
    printf("N[%d] = %d\n", i, vetor2[i]);
  }
  return 0;
}