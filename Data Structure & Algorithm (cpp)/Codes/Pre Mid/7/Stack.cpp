template <typename type>
class Stack{
	type *val;
	int position, size;
	void resize(){
		size = size * 2;
		type *previousVal = val;
		val = new type[size];
		for (int i = 0 ; i < position ; i++)	val[i] = previousVal[i];
		delete []previousVal;
	}
public:
	Stack(int s = 100){	
		if (s < 0)	throw("Illegal Parameter");
		size = s;
		position = 0;
		val = new type[size];
	}
	type push(const type& element){
		if (position == size)	resize();
		val[position++] = element;
		return element;
	}
	type top() const{
		if (empty())	throw("Illegal Operation");
		return val[position - 1];
	}
	void pop() {
		if (empty())	throw("Illegal Operation");
		position--;
	}
	bool empty() const{
		return (position == 0);
	}
};

