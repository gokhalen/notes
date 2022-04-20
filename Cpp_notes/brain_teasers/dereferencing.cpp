#include <iostream>
using namespace std;

int main()
{
  int x[5] = {5,6,7,8,9};
  // Dummy00001's comment - https://stackoverflow.com/questions/3473675/are-negative-array-indexes-allowed-in-c
  cout<<2[x];  // this is equiv to *(x+2)
}
