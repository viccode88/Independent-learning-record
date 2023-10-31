#include <iostream>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(0);
    cout << ceil(b/(a*1.0))<<endl;
}