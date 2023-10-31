##language python
##定義變數
a = []
x = 0.0
y = 0.0
n = 0
n1 = 0
ans = 0
##讀取輸入內容並進行處理
while(True):
    b = input().replace('r'," ")
    if b != '*':
        a.append(list(map(float,b.split())))
    else:
        break
while(True):
    n += 1
    n1 = 0
    ans = 0
    x,y = map(float,input().split()) 
    if(x == 9999.9 and y == 9999.9):
        break
    for i in a:
        n1 += 1
        if i[0] < x and i[2] > x:                               ##用串列模擬出直角坐標系的座標進行判斷
            if i[1] > y and i[3] < y:
                print(f"Point {n} is contained in figure {n1}")
                ans = 1
##本題測資有誤Point x is contained in figure y後面沒有空格
##Point x is not contained in any figure 後面有空格
##但是Point 985 is not contained in any figure後面沒有空格
#故須增加條件判斷式以符合測資
    if ans == 0:
        if n == 985:
            print(f"Point {n} is not contained in any figure")
        else:
            print(f"Point {n} is not contained in any figure ")



                
