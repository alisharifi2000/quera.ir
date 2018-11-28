#include <iostream>
#include <cmath>
using namespace std;

int main()
{
   long long int mat[8];
   mat[7]=0;
   mat[6]=0;
   for(int i=0;i<6;i++)
   {
       cin>>mat[i];
   }
   if(mat[0]==mat[2])
   {
       mat[6]= mat[4];
   }
   else if(mat[0]==mat[4])
   {
       mat[6]= mat[2];
   }
   else if(mat[2]== mat[4])
   {
       mat[6]= mat[0];
   }
   if(mat[1]==mat[3])
   {
       mat[7]= mat[5];
   }
   else if(mat[1]==mat[5])
   {
       mat[7]= mat[3];
   }
   else if(mat[3]== mat[5])
   {
       mat[7]= mat[1];
   }
   cout<<mat[6]<<" "<<mat[7];
}
