
nums = [6,2,6,5,1,2]

nums = sorted(nums) # 오름차순으로 정렬
result = 0 # 배열의 두 값중 최소를 저장
answer = 0 # 최소값들의 합

for i in range(0,len(nums),2): # 두 값씩 나눠주기 위해 2씩 증가하는 반복문 실행
    result = min(nums[i],nums[i+1]) 
    answer += result

print(answer)
'''
KeyPoint 
    오름 차순으로 정렬 --> 두 값씩 나눴을때 무조건 최소값들을 합하면 최대 값이 나온다.
'''