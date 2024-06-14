#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

//functions in c++ : Memory allocation works on stack principle : lifo - last in first out
//Prime nos bw a and b using functions


bool isPrime(int num){
    for(int i=2;i<=sqrt(num);i++){
        if(num%i==0){
            return false;
        }
    }
    return true;
}

 
int main(){

    int a,b;
    cout<<"Enter range to find prime between "<<endl;
    cin>>a>>b;   
    for(int i=a;i<=b;i++){
        if(isPrime(i)){
            cout<<i<<endl;
        }
    }


    return 0;
}

