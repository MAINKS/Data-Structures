#include <stdio.h>
#include <iostream> //for including the input output file for execution
using namespace std;

int main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif

    int a,b; // ';' signifies end of this line command
    cout<<"Enter a and b "<<endl;   //  "<<" : insertion operator
    cin>>a>>b;
    cout<<a+b<<"\n";  


    cout<<" Hello world: "<<endl;

    int c;
    char d ='a';
    bool e = true;
    float f=2.2;
    double g=2.2232;
    c=12;
    cout<<"size of c is :"<<sizeof(c)<<endl;
    cout<<"size of d is :"<<sizeof(d)<<endl;
    cout<<"size of e is :"<<sizeof(e)<<endl;
    cout<<"size of f is :"<<sizeof(f)<<endl;
    cout<<"size of g is :"<<sizeof(g)<<endl;



    // if else elseif

    // for a in range(0,a,1){

        int savings;
        cout<<"Enter your Budget"<<endl;
        cin>>savings;
        

        if (savings>10000){
            if(savings>5500){
                cout<<"Roadtrip with Rashmi"<<endl;
            }
            else  if(savings>8000){
                cout<<"Shopping with Rashmi"<<endl;
            }
        } else if (savings>2000){
            cout<<"Neha"<<endl;
        } else{
            cout<<"Party With friends"<<endl;
        }



        // Maximum of 3 numbers
        int A,B,C;
        cout<<" Enter the value of A , B and C "<<endl;
        cin>>A>>B>>C;
        if (A>B){
            if(A>C){
                cout<<"A is greatest"<<endl;
            }
            else{
                cout<<"C is greatest"<<endl;
            }
        }else if (B>A){
            if(B>C){
                cout<<"B is greatest"<<endl;
            }
            else{
                cout<<"C is the greatest"<<endl;
            }
        }else{cout<<"C is greatest"<<endl;}




        // Even or odd
        int n ;
        cout<<"enter no to find even/odd"<<endl;
        cin>>n;
        if (n%2==0){
            cout<<"No is EVEN"<<endl;
        }
        else{
            cout<<"No is ODD"<<endl;
        }



        // Loops in c++ : for loops
        // Print sum of n nos

        int k;
        cout<<"Enter value till sum to be find of"<<endl;
        cin>>k;
        int sum=0;
        for(int i=0;i<=k;i++){
            sum=sum+i;
        }
        cout<<sum<<endl;


        // While loops : works irrespective of condition

        // while(condition is true){
            //body
        // }

        // Using while loop to print only Positive no
        int b;
        cout<<"Enter the no to check : "<<endl;
        cin>>b;
        while(b>0){
            cout<<" The no is :"<<b<<endl;
            cout<<"Enter next no to check :"<<endl;
            cin>>b;
        }
        cout<<"Out of loop due to input being negative"<<endl;


        // Dowhile loop :similar to while but, it runs atleast once as condition are provided afterwards one iteration
        do{
            cout<<" The no is :"<<b<<endl;
            cout<<"Enter next no to check :"<<endl;
            cin>>b;
        }while(b>0);


        // Jump in loops : Break & continue statements
        // Neha wanna go out based on day and pocketmoney she have, we will use break and continue as:
        int pocketmoney,date;
        cout<<"Enter your Pocketmoney"<<endl;
        cin>>pocketmoney;
        cout<<"What date is today"<<endl;
        cin>>date;

        for(date=1;date<=30;date++){
            if(date%2==0){    //can only go on even days
                continue;
            }
            if(pocketmoney==0){   //won't be able to go if pocketmoney =0
                break;
            }
            cout<<"You can go out today"<<endl;
            pocketmoney=pocketmoney-3000;   //each out reduces pocketmoney by 3000
        }
        cout<<"You can't go out today"<<endl;



        // Prime or Non prime
        int n;
        cout<<"Enter no to check"<<endl;
        cin>>n;
        int i;
        for (i=2; i<n; i++)
        {
            if(n%i==0){
                cout<<"Non prime"<<endl;
                break;
            }
        }
        if(i==n){
            cout<<"Prime"<<endl;
        }
        

        // Print prime nos bw two given numbers

        int a,b;
        cout<<"Enter a and b :"<<endl; 
        cin>>a>>b;

        int i;
        for(int num=a;num<b;num++){
            for(i=2;i<num;i++){
                if(num%i==0){
                    break;
                }
            }
            if(i==num){
                cout<<"Prime nos are :"<<num<<endl;
            }
        }



        // Switch case statements
        char button;
        cout<<"enter any character"<<endl;
        cin>>button;

        switch (button)
        {
        case 'a':
            cout<<"hello"<<endl;
            break;
        case 'b':
            cout<<"Namaste"<<endl;
            break;

        case 'c':
            cout<<"Salut"<<endl;
            break;
        case 'd':
            cout<<"Hola"<<endl;
            break;
        case 'e':
            cout<<"Ciao"<<endl;
            break;
        case 'f':
            cout<<"Bonjour"<<endl;
            break;

        
        default:
            cout<<"I am learning more :: "<<endl;
            break;
        }



    //    Simple Calcuator using switch case
       float n1,n2; //float for decimal input alsos
       cout<<"Enter 2 nos"<<endl;
       cin>>n1>>n2;
       cout<<"Enter the operator to perform"<<endl;
       char op;
       cin>>op;

       switch(op){

        case '+':
            cout<<n1+n2<<endl;
            break;
         case '-':
            cout<<n1-n2<<endl;
            break;
         case '*':
            cout<<n1*n2<<endl;
            break;
         case '/':
            cout<<n1/n2<<endl;
            break;

    //     default:
    //         cout<<"Working on more operators :: "<<endl;
    //         break;

    //    }


//Binary operator - (+,-) for two operands (a+b etc)
//Unary Operator : ++,-- for one operand (a or b)

    int a = 10;
    int b;
    b=a++;   // first value of a used in b then incremented to 11 , b=10
    cout<<b<<endl;
    b=++a;   // value of a is incremented to 11 then used in b , b=11+1=12
    cout<<b<<endl;

    return 0;  //signifies function end


    // logical opertors >,<,==,&&(and),|| (or),!= (not equal), !(not)
    // Bitwise Operator , & (and) : both true = true else false
    //  | (or) : either one of value is true = true
    // ^ (xor) : both values same = 0 , different gives 1
    // ~ (ones) : gives reverse bit 0=1 , 1=0

    // a+=b , a=a+b and same for -,*,/
    // Ternary operator , condition?a:b   Ex: int c=a>b?a-b:b-0;  if condn is true , provides left value else right one

}

// int datatype : 4 bytes , 1 byte = 8 bits , 4 byte = 32 bits (for int datatype)
// Most significant bit(MSB) : 0 for +ve , 1 for -ve 
// Float : 4 bytes , double : 8 bytes , char : 1 byte , boolean : 1 byte (True 1 ,false 0)
