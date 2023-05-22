def solution(brown, yellow):
    answer = []
    total = brown + yellow
    # 갈색 카펫과 노란색 카펫의 수를 합한 값을 total 변수에 저장합니다.

    for b in range(1,total+1):
        # b를 1부터 total까지 반복합니다. b는 카펫의 세로 길이를 나타냅니다.

        if (total / b) % 1 == 0:
            # total을 b로 나눈 결과의 나머지가 0이면, 즉, total을 b로 나누어 떨어지면 실행합니다.
            a = total / b
            # a는 total을 b로 나눈 값으로 카펫의 가로 길이를 나타냅니다.

            if a >= b:
                # a가 b보다 크거나 같은 경우 실행합니다.
                if 2*a + 2*b == brown + 4:
                    # 가로 길이와 세로 길이를 이용하여 갈색 카펫의 수를 계산합니다.
                    # 2*a + 2*b는 카펫의 둘레를 나타내며, brown + 4는 주어진 갈색 카펫의 수에 대한 조건입니다.
                    return [a,b]
                    # 조건을 만족하는 가로와 세로 길이를 반환합니다.
    
    return answer
    # 조건을 만족하는 가로와 세로 길이를 찾지 못한 경우, 빈 리스트인 answer를 반환합니다.