#include <iostream>

using namespace std;

int main()
{
  int n;
  cin>>n;
  string mat [n];
  for(int i=0;i<n;i++)
  {
      cin>>mat[i];
  }
  for(int i=n-1;0<=i;i--)
  {
      if(i==0)
      {
        cout<<mat[i];
      }
      else
      {
        cout<<mat[i]<<" ";
      }
  }
}
