from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    
    total_time = 0 # 걸리는 total 시간 
    qSum = 0 # 다리 weight 

    while truck_weights:
        qSum -= q.popleft() # 빠져나온 트럭 무게 제거 
        total_time+=1 # 트럭은 1씩 움직이므로,  while문이 돌아가는 시간 만큼 time 추가

        if (qSum + truck_weights[0])>weight: # 현재 다리 weight + 다음 트럭 무게가 weight를 넘으면
            q.append(0) # 다리에 다음 트럭 올라갈 수 없으므로 0을 추가 

        else:# 다음 트럭이 올라갈 수 있으면 
            next = truck_weights.pop(0) # 다음 트럭 나옴
            qSum += next  # 다음 트럭 무게 추가 
            q.append(next) # 다음 트럭 queue에 추가 
    
    return total_time + len(q) # 다리를 빠져오지 못한 트럭 + total 시간 

# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     dq = deque(truck_weights)
#     answer = 0
#     bl = bridge_length
#     pl_lst = []
#     while dq:
#         pl = dq.popleft()
        
#         print("pl",pl)
#         bl -= 1
#         print("bl",bl)
#         if pl_lst:
#             if pl_lst[0] + pl > weight:
#                 dq.appendleft(pl)
#             else:
#                 pl_lst.append(pl)
#         else:
#             pl_lst.append(pl)
#         if bl <=0:
#             bl = bridge_length
#         if dq == []:
#             break
#     print(pl_lst)
#         # pl2 = dq.popleft()
#         # print("pl2",pl2)
#         # if pl + pl2 > weight:
#         #     pl2.appendleft(dq)
        

    
#     return answer

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]