#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

int sum(int n){
    int ans=0;
    for(int i=1;i<=n;i++){
        ans += i;
    }
    return ans;
}

int main(){
    int n;
    cout<<" Enter till sum to be calculated"<<endl;
    cin>>n;
    cout<<"Value of sum is " <<sum(n)<<endl;
    
    return 0;
}