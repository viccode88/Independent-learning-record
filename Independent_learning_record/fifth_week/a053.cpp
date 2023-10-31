#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main(){
    int h;
    cin>>h;
    if (h >= 40){
        cout<<"100"<<endl;
    }else if(h > 20){
        cout<<80+(h-20)<<endl;
    }else if(h > 10){
        cout<<60+(h-10)*2<<endl;
    }else{
        cout<<h*6<<endl;
    }
}