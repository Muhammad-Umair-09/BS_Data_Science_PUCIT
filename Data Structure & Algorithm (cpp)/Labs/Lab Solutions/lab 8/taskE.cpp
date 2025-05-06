#include <iostream>
using namespace std;

struct Node{
	int data;
	Node *next;//TO point to next node, null otherwise
	//With default value of parameter, we can use the constructor with two as well as one parameter
	Node (int d, Node *n=NULL){
		data = d;
		next = n;
	}
};

class LinkedList{
	Node *head;
public:
	LinkedList(){head = NULL;	}
	
	LinkedList& addNodeAtStart(int d){
		head = new Node(d, head);//In Node constructor either next will point to NULL or some node previously pointed by head
		return *this;
	}
	LinkedList& addNodeAtEnd(int d){
		if (!head)
			head =new Node(d);
		else{
			Node *t;
			for (t = head ; t -> next != NULL ; t = t -> next);
			t -> next = new Node (d);
		}
		return *this;
	}
	LinkedList& deleteNodeFromStart(){
		if (head!=NULL){
			Node *t = head;
			head = head -> next;
			delete t;
		}
		return *this;
	}
	LinkedList& deleteNodeFromEnd(){
		if (!head)	return *this;	//there is no node to delete
		if (head -> next == NULL){
			delete head;
			head = NULL;
		}
		else{
			Node *t = head;
			for ( ; t -> next -> next != NULL; t = t -> next );//Move to second last node
				delete t->next;
				t->next = NULL;
		}
		return *this;
	}
	void show(){
		for ( Node *t = head ; t != NULL ; t = t -> next )
			cout << t -> data << ' ';
		cout << '\n' ;
	}

    void print(Node *t){
        if (t){
            cout<<t->data<<' ';
            if (t->next)
                t=t->next;
            print(t->next);
            
        }
    }

    void recShow(){
        print(head);
        // cout<<"error";
    }
};



int main(){
    LinkedList l1;
    l1.addNodeAtEnd(1);
    l1.addNodeAtEnd(2);
    l1.addNodeAtEnd(3);
    l1.addNodeAtEnd(4);
    l1.addNodeAtEnd(5);
    l1.addNodeAtEnd(6);
    l1.addNodeAtEnd(7);
    // l1.show();
    l1.recShow();
    return 0;
}