#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

void fib(int num){
    int t1=0;
    int t2=1;
    int nextterm;

    for(int i=1;i<=num;i++){
        cout<<t1<<endl;
        nextterm=t1+t2;
        t1=t2;
        t2=nextterm;
    }

    return;
}

int main(){
    
    int n;
    cout<<"Enter the no till fibonaaci is to be calculated : "<<endl;
    cin>>n;
    cout<<"The fibonacci number are as : "<<endl;
    fib(n);



}