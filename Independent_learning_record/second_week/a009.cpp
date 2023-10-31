//language cpp
#include <iostream>
using namespace std;
int main(){
   char r[1000];            //定義變數
   fgets(r,1000,stdin);     //讀取輸入文字
   for (char &c : r)        //迴圈，一個字一個轉換
   {
    if (c == '\n'){         //轉換結束的條件
        break;
    }else{                  
        c -= 7;             //從範例測資中可得知K = 7
    }
    
   cout << r;               //輸出答案
}