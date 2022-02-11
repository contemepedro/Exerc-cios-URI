#include <stdio.h>

int intercala (int v[],int p,int q,int r)
{
  int i, j, k;
  int count = 0;
  int w[r-p];
  i = p; j = q; k = 0;
  
  while(i<q && j<r)
  {
    if(v[i] <= v[j])
    {
      w[k++] = v[i++];
    }
    else
    {
      w[k++] = v[j++];
      count += q-i;
    }
  }
    while(i < q) 
    {
      w[k++] = v[i++];
    }
    while(j < r) 
    {
      w[k++] = v[j++];
    }
    for (i = p; i < r; i++)
    {
      v[i] = w[i-p];
    }
    return count;
}

int count_mergesort (int v[],int p,int r)
{
    int q, count1 = 0, count2 = 0, count3 = 0;
    if(p < r-1)
    {
        q = (p+r)/2;
        count1 = count_mergesort(v,p,q);
        count2 = count_mergesort(v,q,r);
        count3 = intercala(v,p,q,r);

    }
    return count1 +  count2+ count3;
}
int vet[100000];

int main()
{
  int i, n;
  while(1)
  {
    scanf("%d",&n);
    if (n == 0)
    {
      break;
    }
    for (i = 0; i < n; i++)
    {
      scanf("%d",&vet[i]);
    }    
    int j = count_mergesort(vet,0,n);
    if(j%2==0)
    {
      printf("Carlos\n");
    } 
    else
    {
      printf("Marcelo\n");
    }
  }
  return 0;
}