#include <stdio.h>
#define MAX 10

int main(void)
{
  int vetor[MAX];
  int valor, i;

  for(i=0; i<10; i++)
  {
    scanf("%d", &valor);
    vetor[i] = valor;
  }   
  for (i=0; i<10; i++)
  {
    if (vetor[i] <= 0)
    {
      vetor[i] = 1;
    }
    printf("X[%d] = %d\n", i, vetor[i]);
  }
  return 0;
}