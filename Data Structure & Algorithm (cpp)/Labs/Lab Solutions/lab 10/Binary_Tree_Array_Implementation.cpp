#include <iostream>

using namespace std;

#define SEN 0

// void preOrder(const char *x, int i, const int& END){
// 	if (i >= END || x[i] == SEN)	return;
// 	cout << x[i] << ' ';
// 	preOrder(x, i * 2, 14);
// 	preOrder(x, i * 2 + 1, 14);
// }
// void inOrder(const char *x, int i, const int& END){
// 	if (i >= END || x[i] == SEN)	return;
// 	inOrder(x, i * 2, 14);
// 	cout << x[i] << ' ';
// 	inOrder(x, i * 2 + 1, 14);
// }
// void postOrder(const char *x, int i, const int& END){
// 	if (i >= END || x[i] == SEN)	return;
// 	postOrder(x, i * 2, 14);
// 	postOrder(x, i * 2 + 1, 14);
// 	cout << x[i] << ' ';
// }

int count(const int *x, int i, const int& END){
	if (i>=END ) return 0;
	int left=count(x, i*2, END);
	int right=count(x, i*2 + 1, END);
	if (x[i]!=SEN)return left+right+1;
	return left+right;
}

int count(const int *x, int i, const int& END, int& cnt ){
	if (i>=END ) return 0;
	if (x[i]!=SEN)cnt++;
	count(x, i*2, END,cnt);
	count(x, i*2 + 1, END,cnt);
}


int searchNode(const int *x, int i, const int& END,const int& T ) {
    if (i >= END || x[i] == SEN) return -1;
    if (x[i] == T)return i;
    int lR=searchNode(x,i*2,END,T);
    if (lR != -1)return lR;
    return searchNode(x,i*2+1,END,T);
    }

	int findLargest(const int *x, int i, const int& END ) {
    	if (i >= END || x[i] == SEN) return -1;
    	int leftMax = findLargest(x,i*2,END);
    	int rightMax = findLargest(x,i*2+1,END);
		if (leftMax==-1 && rightMax==-1) return x[i];
		else if (rightMax==-1) return max(leftMax,x[i]);
    	return max(x[i], rightMax);
    }

int countOccurencce(const int *x, int i, const int& END, int T ){
	if (i>=END ) return 0;
	int left=countOccurencce(x, i*2, END,T);
	int right=countOccurencce(x, i*2 + 1, END,T);
	if (x[i]!=SEN && x[i]==T)return left+right+1;
	return left+right;
}


int compareSubtrees(const int *x, int i, const int& END){
    if (i >= END )return 0; 

    int left= compareSubtrees(x, 2 * i, END);
    int right = compareSubtrees(x, 2 * i+1, END);
    if (x[i] != SEN ){
    cout << "Node " << x[i] << ": ";
    if (left == right)cout << "Equal\n"; 
	else if (left > right)cout << "Left Heavy\n";
	else cout << "Right Heavy\n";
	return left+right+1;
	}
	else{
		return left+right;
	}
}


int main(){
	// char x[] = {SEN,'a','b','c','d','e','f',SEN, SEN, 'g','h',SEN,'i','j'};
	int x[] = {SEN,1,2,3,4,5,6,SEN, SEN, 7,8,SEN,9,10};

	cout<<endl;		//way one to count nodes
	int n= count(x,1,14);
	cout<<"No. of Nodes: "<<n<<endl;
	
	int c=0;		//2nd way to count nodes
	count(x,1,14,c);
	cout<<"No. of Nodes: "<<c<<endl;

	char T=10;			//search node
	int n1= searchNode(x,1,14,T);
	cout<<"Node index: "<<n1<<endl;

	int f=findLargest(x,1,14);
	cout<<"MAx is: "<<f<<endl;

	int T1=9;
	int cnt=countOccurencce(x,1,14,T1);
	cout<<"target occurs: "<<cnt<<endl;

	compareSubtrees(x,1,14);

	

	return 0;
}
