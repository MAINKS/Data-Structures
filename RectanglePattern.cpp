#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;


int main(){

    int row ,col;
    cout<<"Enter no of rows and columns"<<endl;
    cin>>row>>col;

    for(int i=1;i<=row;i++){
        for(int j=1;j<=col;j++){
            cout<<"*";
        }
        cout<<endl;
    }


    //hollow rectangle pattern
cout<<endl;
cout<<endl;
cout<<endl;

    for(int k=1;k<=row;k++){
        for(int l=1;l<=col;l++){
            if(k==1 || k==row || l==1 || l==col){
                cout<<"*";
            }
            else{
                cout<<" ";
            }

        }
        cout<<endl;
    }


    return 0;
}