#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

bool check(int x, int y, int z){
    int a = max(x,max(y,z));
    

}

int main(){
    int x,y,z;
    cout<<" Enter three integers to check as pythagorean triplet"<<endl;
    cin>>x>>y>>z;
    
    if (check(x,y,z)){
        cout<<"Pythagorean triplet"<<endl;
    }else{
        cout<<"Not a pythagorean triplet"<<endl;
    }
    
    return 0;
}