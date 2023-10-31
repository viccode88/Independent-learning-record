#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main(){
    int h,m,s,t;
    int total = 0;
    cin>>h>>m>>s>>t;
    total += (h * 3600) + (m * 60) + s + (t * 5400);
    h = floor(total/3600);
    m = floor((total%3600)/60);
    s = (total - m*60 - h*3600);

    // cout.setf(ios::fixed,ios::floatfield);
    // cout.precision(0);
    cout << h%36<<":"<<setw(2)<<setfill('0')<<m<<":"<<setw(2)<<setfill('0')<<s<<endl;
}