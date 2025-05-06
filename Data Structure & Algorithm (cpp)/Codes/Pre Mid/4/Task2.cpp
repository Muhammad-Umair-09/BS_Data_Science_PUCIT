#include <iostream>
#include <stack>

using namespace std;

int calc(int x, int y, char op){
	if (op == '+')		return x + y;
	else if (op == '-')	return x - y;
	else if (op == '*')	return x * y;
	else if (op == '/')	return x / y;
	else if (op == '%')	return x % y;
	return 0;
}
int evaluate(string post){
	int result, v1, v2;
	stack<int> s;
	for (char c : post){
		if (c >= '0' && c <= '9')	s.push(c - '0');	//convert character digit to number digit
		else{
			v1 = s.top();	s.pop();
			v2 = s.top();	s.pop();
			result = calc(v2, v1, c);  
			s.push(result);
		}
	}
	return s.top();
}
int main(){
	cout << "2+3*4 = " << evaluate("234*+") << '\n';
	cout << "(2+3)*4 = " << evaluate("23+4*") << '\n';
	cout << "2+3*4/2 = " << evaluate("234*2/+") << '\n';
	cout << "(2+3)*(4-2)/(1+4) = " << evaluate("23+42-*14+/") << '\n';
    return 0;
}

