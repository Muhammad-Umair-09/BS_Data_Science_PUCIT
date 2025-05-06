#include <iostream>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>

using namespace std;

int main(){
	srand(time(0));
	int processes[]={rand()%18 + 2, rand()%18 + 2, rand()%18 + 2, rand()%18 + 2, rand()%18 + 2};
	cout << "Process Times: ";
	for (int t : processes) 
		cout << t << ' ';
	cout << '\n';	
	queue<pair<int, int>> q;
	queue<int> q1;
	for (int i = 0 ; i < 5 ; i++)
		q.push({i, processes[i]});
	while (!q.empty()){
		int n=q.size();
		while ((n/2)>0){
			pair<int, int> p = q.front();
			q.pop();
			if (p.second >= 4)	cout << "Process " << p.first << " processor PF for 4 seconds\n";
			else				cout << "Process " << p.first << " processor PF for " << p.second << " seconds\n";
			if (p.second > 4)	q.push({p.first, p.second - 4});
			else q1.push(p.first);

			pair<int, int> p1 = q.front();
			q.pop();
			if (p1.second >= 4)	cout << "Process " << p1.first << " processor PS for 4 seconds\n";
			else				cout << "Process " << p1.first << " processor PS for " << p1.second << " seconds\n";
			if (p1.second > 4)	q.push({p.first, p1.second - 4});
			else q1.push(p.first);
			n--;
		}
		if (n%2!=0){
			pair<int, int> p = q.front();
			q.pop();
			if (p.second >= 4)	cout << "Process " << p.first << " processor PF for 4 seconds\n";
			else				cout << "Process " << p.first << " processor PF for " << p.second << " seconds\n";
			if (p.second > 4)	q.push({p.first, p.second - 4});
		}
		int i,r=rand()%3;
		if (r>0){
			for (i=0;i<r;i++) {
				int t=rand()%18 + 2;
				if (!q1.empty()){
					q.push({q1.front(),t});
				cout<<"Process "<<q1.front()<<" time "<<t<<" seconds\n";
					q1.pop();
			}
			else cout<<"Process "<<q.size()<<" time "<<t<<" seconds\n";
			
		}
	}
	else{
		cout<<"No new process\n";
	}
	}
	return 0;
}
