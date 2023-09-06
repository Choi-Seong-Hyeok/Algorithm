N = int(input())

danzi = [] # 지도의 크기
total_danzi = 0 # 총 단지수
house_cnt = 0 # 단지내 집의 수
house_list = [] # 단지내 집의 수 리스트


for _ in range(N): # 단지 입력받기
    val = list(map(int,input()))
    danzi.append(val)


def dfs(x,y):
    global house_cnt
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if danzi[x][y] == 1:
        danzi[x][y] = 0
        house_cnt += 1 
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    



for i in range(N):
    for j in range(N):
        if danzi[i][j] == 1:
            house_cnt = 0
            if dfs(i,j) == True:
                total_danzi += 1
                house_list.append(house_cnt) 

print(total_danzi)
house_list = sorted(house_list) # 오름차순 정렬
for i in house_list:
    print(i)











