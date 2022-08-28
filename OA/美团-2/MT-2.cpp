#include <iostream>
using namespace std;
int main()
{
  int n, x1, y1, x2, y2, x3, y3, l1, l2, l3;
  cin>>n>>x1>>y1>>x2>>y2>>x3>>y3>>l1>>l2>>l3;
  int x=1, y=1;
  int flag = 0;
  for(x=max(1, x1-l1);x<=min(n, x1+l1);x++)
  {
    int y11=y1-l1+abs(x1-x), y12=y1+l1-abs(x1-x);
    if(abs(x-x1)+abs(y11-y1) == l1 && abs(x-x2)+abs(y11-y2) == l2 && abs(x-x3)+abs(y11-y3) == l3)
    {
      cout<<x<<" "<<y11<<endl;
      break;
    }
    if(abs(x-x1)+abs(y12-y1) == l1 && abs(x-x2)+abs(y12-y2) == l2 && abs(x-x3)+abs(y12-y3) == l3)
    {
      cout<<x<<" "<<y12<<endl;
      break;
    }
  }
}
