a = input()
b = ""
c = 0
if len(a)%2 == 0:
    for i in range(len(a)//2):
        if (a[i-1] == a[-i]):
            b += a[i]
        else:
            print("NO")
            break
    if(len(a)//2 == len(b)):
        print("YES")
        print(b)
else:
    print("NO")
        