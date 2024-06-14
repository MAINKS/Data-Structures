#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

int main(){
    //inverted half pyramid 

    int n;
    cout<<"enter value for pyramid to form"<<endl;
    cin>>n;

    for(int a=n;a>=1;a--){
        for(int b=1;b<=a;b++){
            cout<<" * ";
        }
        cout<<endl;
    }


cout<<endl;
cout<<endl;
cout<<endl;
cout<<endl;


    //Inverted half 180 rotated pyramid
     for(int i=1;i<=n;i++){
        for(int j =1;j<=n;j++){
            if(j<=n-i){             //as in first row , first 4 columns are spaces = n-i for each columns
                cout<<" ";
            }
            else{
                cout<<"*";
            }
        }
        cout<<endl; 
     }


cout<<endl;
cout<<endl;
cout<<endl;
cout<<endl;


// pyramid with nos

     for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout<<i<<"  ";
        }cout<<endl;
     }



cout<<endl;
cout<<endl;
cout<<endl;
cout<<endl;



//Increasing number pyramid   : floyd's triangle
      int count;
      for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout<<count<<"  ";
            count++;
        }cout<<endl;
     }



    // Butterfly pattern : Imp
    //no of stars = no of rows 
    // space = 2n-2(row no)

//for upper part of pyramid

    for(int i =1;i<=n;i++){
        for(int j =1;j<=i;j++){
            cout<<"*";
        }
        int space=2*n-2*i;
        for(int j=1;j<=space;j++){
            cout<<" ";
        }
        for(int j=1;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }

    //for lower part of pyramid
    for(int i =n;i>=1;i--){        //change in i no of rows initialisation
        for(int j=1;j<=i;j++){
            cout<<"*";
        }
        int space=2*n-2*i;
        for(int j=1;j<=space;j++){
            cout<<" ";
        }
        for(int j=1;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }


    // inverted pattern using nos
    // rows = 1 to n
    // columns = (n+1)-rowno
    // elements = column no only

    for (int i =1;i<=n;i++){
        for (int j =1;j<=n+1-i;j++){
            cout<<"*";
        }
        cout<<endl;
    }

    //0-1 pyramid pattern
    //Row : 1 to n 
    //column : 1 to rowno
    //elements : see when rowno+colno are added = gives even no always with element as 1 on that position

    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            if((i+j)%2==0){
                cout<<" 1 ";
            }
            else{
                cout<<" 0 ";
            }
        }
        cout<<endl;
    }

    //Rhombus pattern 
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=n;j++){
            cout<<"*";
        }
        cout<<endl;
    }


    //number pattern heap
    //row : 1 to n
    //column : for spaces : 1 to n-rowno
    //       : for nos : 1 to rowno

    for(int i =1;i<=n;i++){
        for (int j =1;j<=n-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=i;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }


//Palindromic pattern : important 
    //row : 1 to n
    //columns : for spaces: 1 to n-rowno
    //        : for decreasing nos : k=rowno ,k-- , n-rowno to n
    //        : for increasing nos : k=2 ; k++ ; n to n+rowno-1

    for(int i=1;i<=n;i++){
        int j;
        for(j=1;j<=n-i;j++){
            cout<<"  ";
        }
        int k=i;
        for(;j<=n;j++){
            cout<<k--<<" ";
        }
        k=2;
        for(;j<=n+i-1;j++){
            cout<<k++<<" ";
        }
        cout<<endl;
    }

    //Star pattern
    // rows: 1 to n
    // columns : 1st part - spaces : from 1 to (n-rowno(i))
    //         : 2nd part - stars : from : odd no of stars : from 1 to (2rowno-1)
    // for inverse part , we be using same condition but in reverse direction

    for(int i =1;i<=n;i++){
        for(int j =1;j<=n-i;j++){       //for upper part of the star pattern
            cout<<" "; 
        }
        for(int j=1;j<=2*i-1;j++){
            cout<<"*";
        }
        cout<<endl;
    }

    for(int i =n;i>=1;i--){
        for(int j =1;j<=n-i;j++){       //for lower part of the star pattern
            cout<<" "; 
        }
        for(int j=1;j<=2*i-1;j++){ 
            cout<<"*";
        }
        cout<<endl;
    }

    // Zig zag pattern  : kinda imp 
    // rows 1 to3 , column position prints * if position (i+j)/4 gives 0 or row =2 and column no/4 =0
    for(int i=1;i<=3;i++){
        for(int j=1;j<=n;j++){
            if(((i+j)%4==0) || (i==2 && j%4==0)){
                cout<<" "<<"*"<<" ";
            }
            else{
                cout<<" ";
            }
        }
        cout<<endl;
    }


return 0;

}