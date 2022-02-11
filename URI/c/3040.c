#include <stdio.h>
int main()
{
  int altura, diametro, galhos;
  int n, i, cont;

  scanf("%d", &n);
  for (i=0; i<n; i++)
  {
    cont = 0;
    scanf("%d %d %d", &altura, &diametro, &galhos);
    if (altura >= 200 && altura <= 300)
    {
      cont += 1;
    }
    if (diametro >= 50)
    {
      cont += 1;
    }
    if (galhos >= 150)
    {
      cont += 1;
    }
    if (cont == 3)
    {
      printf("Sim\n");
    }
    else
    {
      printf("Nao\n");
    }
  }
  return 0;
}