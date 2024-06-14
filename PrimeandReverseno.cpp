#include <stdio.h>
#include <iostream> //for including the input output file for execution
#include <cmath>
using namespace std;

int main(){
    
    int n;
    cout<<"Enter no to check as prime or not"<<endl;
    cin>>n;
    bool flag=0;
    
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0){
            flag=1;
            cout<<"Non prime: "<<endl;
            break;
        }
    }
    if(flag==0){
        cout<<"Prime"<<endl;
    }

//Reversing a number
    cout<<"Enter no to reverse : "<<endl;
    cin>>n;

    int reverse=0;
    while(n>0){
        int lastdigit = n%10;
        reverse = reverse*10 + lastdigit;
        n=n/10;
    }
    cout<<"Reversed number is : "<< reverse <<endl;

//Armstrong no = sum of cube of the digits is equal to number itself ; 153 = 1ˆ3+5ˆ3+3ˆ3 = 153 only

    int sum;
    int originaln =n;
    cout<<"Enter no to check as armstrong or not : "<<endl;
    cin>>n;


    while(n>0){
        int lastdigit = n%10;
        sum+= pow(lastdigit,3);
        n=n/10;

    }
    if(sum==originaln){
        cout<<"Armstrong no"<<endl;
    }
    else{
        cout<<"Not an Armstrong no"<<endl;
    }

    
    return 0;

}