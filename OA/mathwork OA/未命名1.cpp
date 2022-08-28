#include<iostream>
using namespace std;
int main()
{
	int maxLength=2;
	int path[3]=[10,-20,-5];
	int lens=path.size();
	int dp[lens];
	for(int i=0;i<lens;i++)
		dp[i]=0;
	dp[0]=path[0];
	vector<int> queue;
	queue.push_back(dp[0]);
	int maxtemp=0;
	for(int i=0;i<lens;i++)
	{
		if(i<maxlength)
		{
			dp[i]=queue[queue.size()-1]+path[i];
			queue.push_back(dp[i]);
		}
		else
		{
			dp[i]=queue[queue.size()-1]+path[i];
			queue.push_back(dp[i]);
			
		}
		dp[i]=maxtemp+path[i];
		queue.
		
	}
	return dp[0];
}
