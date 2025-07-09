def solution(S):
    
    max_sum = 0

    for i in range(len(S) - 1):
        first = S[i:i+2]

        for j in range(len(S) - 1):
            
            if abs(i - j) >= 2:
                second = S[j:j+2]
                total = int(first) + int(second)
                if total > max_sum:
                    max_sum = total

    return max_sum


print(solution("43798"))     
    
