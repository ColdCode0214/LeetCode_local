#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	int a[3][2]={{1,2},{2,3},{3,1}};
	sort(a,a+3);
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<2;j++)
			cout<<a[i][j]<<" ";
		cout<<endl;
	}
}
