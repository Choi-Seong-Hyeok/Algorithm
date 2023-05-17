def solution(tickets):
    answer = []  # 정답을 저장할 리스트
    
    visited = [False]*len(tickets)  # 각 티켓을 사용했는지 여부를 저장할 리스트
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:  # 모든 티켓을 사용한 경우 (출발지점 ICN 고정 + 1)
            answer.append(path)  # 정답 리스트에 경로 추가
            return
        
        for idx, ticket in enumerate(tickets):  # 모든 티켓을 확인하며
            if airport == ticket[0] and visited[idx] == False:  # 출발지가 현재 공항과 같고, 아직 사용하지 않은 티켓인 경우
                visited[idx] = True  # 해당 티켓 사용 여부 업데이트
                dfs(ticket[1], path+[ticket[1]])  # 도착지를 새로운 출발지로 하여 DFS 수행
                visited[idx] = False  # DFS가 끝나면 사용 여부 업데이트
    
    dfs("ICN", ["ICN"])  # 출발지가 "ICN"인 경로부터 시작
    
    answer.sort()  # 경로를 알파벳 순으로 정렬
    
    return answer[0]  # 가장 알파벳 순서가 빠른 경로 반환
