#include <iostream>
#include <string>
using namespace std;

int main()
{
   string word;
   cin>>word;
   cout<<word<<endl;
   for(int i=1;i<word.size();i++)
   {
       for(int j=0;j<=i;j++)
       {
           word[j]=word[i];
       }

       if(i==word.size()-1)
       {
           cout<<word;
       }
       else
       {
            cout<<word<<endl;
       }

   }

}
