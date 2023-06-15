from collections import deque


def solution(priorities, location):
    # 1. 위치 고려하기
    # 2. 우선순위 고려하기
    que = deque(priorities)
    answer = 0
    while True:
        m = max(que) # 최대값 구하기
        popleft = que.popleft() # 왼쪽 제거하고
        location -= 1 
        ## 
        # priorities = [1, 3, 2]  왼쪽 2 제거 됌
        # location = -1
        # max = 3
        ##
        if popleft != m:  # 2 != 3
            que.append(popleft)  # 다시 오른쪽 붙이기 [1, 3, 2, 2]
            if location < 0:
                location = len(que) -1  # location = 1 이니까 패스
        else:
            answer += 1
            if location < 0:
                break
    return answer
    
priorities = [2, 1, 3, 2]
location = 2
solution(priorities, location)