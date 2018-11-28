#include <iostream>

using namespace std;

int main()
{
    int m1,m2;
    int h1,h2;
    cin>>h1;
    cin>>m1;
    if(m1==0)
    {
        m2=0;
    }
    else
    {
        m2=60-m1;
    }
    if(h1==0)
    {
        h2=0;
    }
    else
    {
        h2=12-h1;
    }
    if(h2<10)
    {
        if(m2<10)
        {
            cout<<"0"<<h2<<":"<<"0"<<m2;
        }
        else
        {
            cout<<"0"<<h2<<":"<<m2;
        }
    }
    else
    {
        if(m2<10)
        {
            cout<<h2<<":"<<"0"<<m2;
        }
        else
        {
            cout<<h2<<":"<<m2;
        }
    }
}
