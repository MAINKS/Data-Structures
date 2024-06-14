#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

//Sum of n natural nos
int Sum(int n){
    int ans=0;
    for(int i=1;i<=n;i++)
        ans+=i;
    return ans;
    cout<<"Sum is : " << ans <<endl;
}

int main(){
    int n;
    cout<<"enter the value of n:";
    cin >> n;
    Sum(n);
}