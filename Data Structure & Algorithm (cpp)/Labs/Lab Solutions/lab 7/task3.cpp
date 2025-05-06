#include <iostream>
using namespace std;

template <typename T>
struct Node{
	T data;
	Node *next;//TO point to next node, null otherwise
    Node *prev;
	//With default value of parameter, we can use the constructor with two as well as one parameter
	Node (T d, Node *n=NULL,Node *p=NULL){
		data = d;
		next = n;
        prev = p;
	}
};

template <typename T>
class DLinkedList
{
	Node<T> *head;
	Node<T> *tail;

public:
	DLinkedList() { head = NULL;tail=NULL; }

	DLinkedList &addNodeAtEnd(T d)
	{
		if (!head){
			head = new Node<T>(d);
            tail = head;
        }
		else
		{
            Node<T> *t= new Node<T>(d);
			tail->next = t;
            t->prev = tail;
            tail = t;
		}
		return *this;
	}

    bool isin(Node<T> *h,T d) const{
        Node<T> *t1=head,*t2=h;
        for (;t1!=t2;t1=t1->next){
            if (t1->data==t2->data)
            return true;
        }
        return false;
    }

    DLinkedList& removeDuplicates(){
        if (!head) return *this;
        Node<T> *cur=tail;
        for(;cur;cur=cur->prev){
            if (isin(cur,cur->data)){
                Node<T> *temp;
                if (cur->prev){
                    temp=cur;
                    cur->prev->next=cur->next;
                    delete temp;
                }
            }
        } 
    }
	
	void show() const
	{
		for (Node<T> *t = head; t != NULL; t = t->next)
			cout << t->data << ' ';
		cout << '\n';
	}
	void revshow() const
	{
		for (Node<T> *t = tail; t != NULL; t = t->prev)
			cout << t->data << ' ';
		cout << '\n';
	}
};

int main(){
    DLinkedList<int> l1;
    l1.addNodeAtEnd(1);
    l1.addNodeAtEnd(1);
    l1.addNodeAtEnd(2);
    l1.addNodeAtEnd(4);
    l1.addNodeAtEnd(9);
    l1.addNodeAtEnd(6);
    l1.addNodeAtEnd(6);
    l1.addNodeAtEnd(3);
    l1.addNodeAtEnd(11);
    l1.addNodeAtEnd(4);
    l1.addNodeAtEnd(4);
    l1.show();
    l1.removeDuplicates();
    l1.show();
    l1.revshow();
}