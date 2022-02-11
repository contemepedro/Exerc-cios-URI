#include <stdio.h>

int main(void)
{
  int n, i, j;
  int vmax[231];

  scanf("%d", &n);
  for(i=0; i<n; i++)
  {
    int m, num, count = 0;

    scanf("%d", &m);
    for (j=0; j<231; j++)
    {
      vmax[j] = 0;
    }
    for (j=0; j<m; j++)
    {
      scanf("%d", &num);
      vmax[num]++;
    }
    for(j=0; j<231; j++)
    {
      if(vmax[j] != 0)
      {
        while(vmax[j] > 0)
        {
          if(count == (m-1))
          {
            printf("%d", j);
            printf("\n");
            vmax[j]--;
            count++;
          }
          else
          {
            printf("%d ", j);
            vmax[j]--;
            count++;
          }
        }
      }
    }
  }
  return 0;
}