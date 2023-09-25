'''
    파일 정리.
    1) 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줌
    2) 확장자들을 사전 순으로 정렬
'''
import sys
N = int(sys.stdin.readline())
files = list()
for _ in range(N):
    val = str(sys.stdin.readline().rstrip())
    files.append(val)

# 확장자 별로 나눠야함
# 1. '.'을 기준으로
extensions = set()
for i in files:
    val = i.split('.')[-1]
    extensions.add(val)

extensions = sorted(list(extensions))
# 2. extensions 기준으로 확장자 파일 개수 cnt
cntList = [0] * len(extensions)

for i in range(len(extensions)):
    for j in range(len(files)):
        file = files[j].split('.')[-1]
        if file == extensions[i]:
            cntList[i] += 1

# 3. 두 리스트 출력
for i in range(len(extensions)):
    print(extensions[i],cntList[i])
