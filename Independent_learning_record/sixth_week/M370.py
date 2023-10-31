#輸入
x,n = map(int,input().split()) 
mc_map = list(map(int,input().split()))
#把x加入mc_map串列並排序
mc_map.append(x)
mc_map_2 = []
mc_map = sorted(mc_map)
#以老鼠位置為基準切割串列
for i in range(n+1):
    if mc_map[0] != x:
        mc_map_2.append(mc_map.pop(0))
    else:
        del mc_map[0]
        break
#尋找兩個串列食物最多的那邊
if len(mc_map) >= len(mc_map_2):
    print(len(mc_map),max(mc_map))
else:
    print(len(mc_map_2),min(mc_map_2))
    
