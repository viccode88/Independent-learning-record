#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int main(){
    int k,w,s,e;
    int ans = 0;
    cin >> k >> w >> s >> e;
    if (k > 1){
        ans += 20 + (k-2)*5;
    }else{
        ans += 20;
    }
    ans += floor((w/2)*5);
    if (s <= 18 and e > 18){
        ans += 185;
    }
    if(s <= 19 and e > 19){
        ans += 195;
    }
    if(s <= 20 and e > 20){
        ans += 205;
    }
    if(s <= 21 and e > 21){
        ans += 215;
    }
    if(s <= 22 and e > 22){
        ans += 225;
    }
    cout << ans;
}