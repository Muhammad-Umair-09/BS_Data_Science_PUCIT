#include <iostream>
#include "Node_Template.cpp"

using namespace std;

template <typename T>
class LinkedList
{
	Node<T> *head;

public:
	LinkedList() { head = NULL; }

	LinkedList &addNodeAtStart(T d)
	{
		head = new Node<T>(d, head);
		return *this;
	}
	LinkedList &addNodeAtEnd(T d)
	{
		if (!head)
			head = new Node<T>(d);
		else
		{
			Node<T> *t;
			for (t = head; t->next != NULL; t = t->next)
				;
			t->next = new Node<T>(d);
		}
		return *this;
	}

	LinkedList &addInOrder(T d)
	{
		if (!head || head->data > d)
			return addNodeAtStart(d);
		else
		{
			Node<T> *t = head;
			while (t->next != NULL && t->next->data < d)
				t = t->next;
			if (!t->next)
				t->next = new Node<T>(d);
			else
			{
				Node<T> *temp = new Node<T>(d);
				temp->next = t->next;
				t->next = temp;
			}
		}
		return *this;
	}

	// LinkedList& removeDuplicatesElements(){
	// 	if (!head || !head->next) return *this;
	// 	Node<T> *t1=head,*t2;
	// 	while (t1->next){
	// 		t2=t1;
	// 		while (t2->next){
	// 			if (t1->data==t2->next->data)
	// 				t2-next=t2->next->next;
	// 		t2=t2->next;
	// 		}
	// 		t1=t1->next;
	// 	}
	// 	return *this;
	// }
	LinkedList &removeDuplicatesElements()
	{
		if (!head || !head->next)
			return *this;
		Node<T> *t1 = head;
		while (t1->next)
		{
			if (t1->data == t1->next->data)
			{
				t1->next = t1->next->next;
				continue;
			}
			t1 = t1->next;
		}
		return *this;
	}

	LinkedList &removeDuplicates()
	{
		if (!head || !head->next)
			return *this;
		Node<T> *s = NULL, *m = head, *e = head->next;
		while (e != NULL)
		{
			while (m->data == e->data)
			{
				T d = m->data;
				if (head->data == m->data)
				{
					while (d == head->data)
						deleteNodeFromStart();
					m = head;
					e = m->next;
				}
				else
				{
					while (m->data == d)
					{
						s->next = e;
						m = e;
						e = e->next;
					}
				}
			}
			s = m;
			m = e;
			e = e->next;
		}
		return *this;
	}

	LinkedList &splitEvenElements()
	{
		Node<T> *temp = head;

		while (temp != nullptr)
		{
			if ((temp->data) % 2 == 0)
			{
				temp->data = (temp->data) - 1;
				int v1 = 1;
				Node<T> *nelement = new Node<T>(v1);
				nelement->next = temp->next;
				temp->next = nelement;
			}
			temp = temp->next;
		}
		return *this;
	}
	LinkedList &mergeElements()
	{
		for (Node<T> *t = head; t != NULL; t = t->next)
		{
			if (t->data >= 50)
				continue;
			else if (t->data <= 50)
			{
				while ((t->data <= 50) && (t->next != NULL))
				{
					t->data += t->next->data;
					t->next = t->next->next;
				}
			}
		}
		return *this;
	}

	LinkedList &deleteNodeFromStart()
	{
		if (head != NULL)
		{
			Node<T> *t = head;
			head = head->next;
			delete t;
		}
		return *this;
	}
	LinkedList &deleteNodeFromEnd()
	{
		if (!head)
			return *this; // there is no node to delete
		if (head->next == NULL)
		{
			delete head;
			head = NULL;
		}
		else
		{
			Node<T> *t = head;
			for (; t->next->next != NULL; t = t->next)
				; // Move to second last node
			delete t->next;
			t->next = NULL;
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
    void print()const{
        Node<T> *t=head;
        for (;t;t=t->next){
            if (isin(t,t->data)==false)
                cout<<t->data<<' ';
        }
        cout<<endl;
    }

	bool check(T d)const{
		Node<T> *t=head;
		for (;t;t=t->next){
			if (t->data==d)
			return true;
		}
		return false;
	}

	LinkedList& UNION(LinkedList& l){
		Node<T> *h1=head,*h2=l.head;
		// if (!h1 || !h2) return *this;

		for (; h1->next ;h1=h1->next);
		// cout<<h2->data<<endl;
		while (h2 -> next){
			if (!check(h2->data)){
				h1->next=h2;
				h1=h1->next;
				h2=h2->next;
				h1->next=NULL;
			}else{
				Node<T> *temp=h2;
				h2=h2->next;
				delete temp;
			}
		}
		// for(Node<T> *h1 = head; h1; h1 = h1 -> next)
		// 	cout << h1 ->data << " ";
		// cout << endl;

		return l;
	}

	
	void show() const
	{
		for (Node<T> *t = head; t != NULL; t = t->next)
			cout << t->data << ' ';
		cout << '\n';
	}

    LinkedList& splitEven(){
        if (!head) return *this;
        Node<T> *t=head;
        for (;t;t=t->next){
            while (t->data%2==0){
                Node<T> *n=new Node<T>(t->data/2);
                t->data=t->data/2;
                n->next=t->next;
                t->next=n;

            }
        }
        return *this;
    }
};

int main()
{
	LinkedList<int> l1,l2;
	
	l1.addNodeAtStart(9);
	l1.addNodeAtStart(12);
	l1.addNodeAtStart(8);
	l1.addNodeAtStart(7);
	l1.addNodeAtStart(6);
	l1.addNodeAtStart(5);

	

	// l1.removeDuplicatesElements();
	// l1.removeDuplicates();
	// l1.splitEvenElements();
	// l1.mergeElements();
	// l1.print();
	l1.show();
    l1.splitEven();
    l1.show();
}
