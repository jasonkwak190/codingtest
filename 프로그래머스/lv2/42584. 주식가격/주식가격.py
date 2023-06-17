def solution(prices):
    answer = []
    for i in range(len(prices)):
        c=0
        for j in range(i+1, len(prices)):
            c+=1
            if prices[i]>prices[j]:
                break;
        answer.append(c)
    return answer