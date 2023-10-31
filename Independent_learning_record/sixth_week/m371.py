global map_list,n,m,ans

n,m = map(int,input().split())
map_list = []
ans = 0
ram = []
for i in range(n):
    
    map_list.append(list(map(int,input().split())))
def look_for(ans_fun):
    haha = 0
    for y in range(n):
        for x in range(m):
            for k in range(1+x,m):
                if map_list[y][x] == map_list[y][k] and map_list[y][x] != -1 :
                    ans_fun += map_list[y][x]
                    haha = 1
                    map_list[y][x] = -1
                    map_list[y][k] = -1
                elif(map_list[y][k] != -1 ):
                    break
    for x in range(m):
        for y in range(n):
            for k in range(1+y,n):
                if map_list[y][x] == map_list[k][x] and map_list[y][x] != -1:
                    ans_fun += map_list[y][x]
                    haha = 1
                    map_list[y][x] = -1
                    map_list[k][x] = -1
                elif(map_list[k][x] != -1 ):
                    break
    if haha == 0:
        return -2
    else:
        return ans_fun
while True:
    ram = look_for(0)
    if ram != -2:
        ans += ram
    else:
        print(ans)
        break