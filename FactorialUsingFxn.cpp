#include <stdio.h>
#include <iostream>             //for including the input output file for execution
using namespace std;

int fact(int n){
    int factorial =1;
    for(int i=1;i<=n;i++){
        factorial=n*fact(n-1);  //using recursion
    }
    return factorial;
}


int main(){

    int n,r;
    cout<<"Enter the value to find factorial of : "<<endl;
    cin>>n;
    int ans =  fact(n);
    cout<<ans<<endl;  
  
    //calculation of n!/r!*(n-r)!
    cout<<"Enter the value of r : "<<endl;
    cin>>r;
    int ans1 = fact(n)/(fact(r)*fact(n-r)); 
    cout<<ans1<<endl;
    
    return 0;
}

// /fact = 5*4*3*2*1!
// n*fact(n-1)