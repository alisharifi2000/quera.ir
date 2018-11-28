#include <iostream>

using namespace std;
int fact(int);
int combine (int,int);
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            cout<<combine(i,j)<<" ";
        }
        cout<<endl;
    }
}
int fact(int n)
{
    if(n==1||n==0)
    {
        return 1;
    }
    else
    {
        return n*fact(n-1);
    }
}
int combine(int n, int k)
{
    return fact(n)/(fact(k)*fact(n-k));
}
