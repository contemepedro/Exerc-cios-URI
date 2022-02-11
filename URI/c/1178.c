#include <stdio.h>

int main(void)
{
  double vetor[100];
  double valor; 
  int i;

  scanf("%lf", &valor);
  vetor[0] = valor;
  for (i=0; i<100; i++)
  {
    printf("N[%d] = %.4lf\n", i, vetor[i]);
    valor /= 2;
    vetor[i+1] = valor;
  }
  return 0;
}