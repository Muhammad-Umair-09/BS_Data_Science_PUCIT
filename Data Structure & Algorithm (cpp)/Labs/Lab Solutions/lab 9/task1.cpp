#include <iostream>
using namespace std;

template<typename T>
class Deque{
    struct Dnode
    {
        T val;
        Dnode *next,*prev;
        Dnode(T v, Dnode *n=NULL,Dnode *p=NULL){
            val=v;
            next=n;
            prev=p;
        }
    };

    Dnode *head;
    int count=0;
public:
    Deque(){
        head= new Dnode(0);
        head->next=head->prev= head;
    }

    void push_front(T val){
        head->next= new Dnode(val,head->next,head);
        head->next->next->prev=head->next;
        count++;
    }

    void pop_front(){
        if (count!=0){
            head->next=head->next->next;
            delete head->next->prev;
            head->next->prev=head;
            count--;
        }
    }

    void pop_back(){
        if (count!=0){
            head->prev=head->prev->prev;
            delete head->prev->next;
            head->prev->next=head;
            count--;
        }
    }

    void push_back(T val){
        head->prev=new Dnode(val,head,head->prev);
        head->prev->prev->next=head->prev;
        count++;
    }

    T front() const{
        if (count==0) throw("NoNode");
        return head->next->val;
    }
    
    T back()const{
        if (count==0) throw("NoNode");
        return head->prev->val;
    }

    void clear(){
        head=head->next;
        for (;count>0;count--){
            head=head->next;
            delete head->prev;
        }
        head->next=head->prev=head;
    }

    int size() const{
        return count;
    }

    bool isempty()const{
        if (count==0) return true;
        return false;
    }

    void show(){
        Dnode *t=head->next;
        while (t!=head){
            cout<<t->val<<' ';
            t=t->next;
        }
        cout<<endl;
    }
    
};

int main(){
    Deque<int> dq;
    cout<<"empty "<<dq.isempty()<<endl;
    dq.push_front(2);
    dq.push_front(9);
    dq.push_front(2);
    dq.push_back(6);
    dq.push_front(4);
    dq.push_back(11);
    cout<<"size "<<dq.size()<<endl;
    dq.show();
    cout<<"empty "<<dq.isempty()<<endl;


    cout<<"front "<<dq.front()<<endl;
    dq.pop_front();
    cout<<"front "<<dq.front()<<endl;
    cout<<"back "<<dq.back()<<endl;
    dq.pop_back();
    cout<<"back "<<dq.back()<<endl;

    cout<<"size "<<dq.size()<<endl;
    dq.show();
    dq.clear();
    dq.show();
    cout<<"size "<<dq.size()<<endl;


}

