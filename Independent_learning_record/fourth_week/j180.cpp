#include  <iostream>
#include <array>
#include <iterator>
#include <cmath>
using namespace std;
int a[1000],b[1000];
int n = 0;
int and_num = 0;
int ans;
int main()
{
    while(true){
        ans = 0;
        cin >> a[n] >> b[n];
        if(a[n] == -1 or b[n] == -1){
            break;
        }
        if(a[n] == 0 or b[n] == 0){
            cout <<ans<< endl;
            continue;
        }
        and_num = a[n]*b[n];
        
        while (true)
        {
            ans += 1;
            and_num -= ceil((and_num*1.0)/b[n]) ;
            if (and_num <= 0){
                break;
            }
        }
        cout <<ans<< endl;
        n += 1;
    }   
    return 0;
}
