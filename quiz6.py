def solution(S):
    S = list(S) 
    n = len(S)

    for i in range(n // 2):
        left = S[i]
        right = S[n - 1 - i]

        if left == '?' and right == '?':
            S[i] = S[n - 1 - i] = 'a' 
        elif left == '?':
            S[i] = right
        elif right == '?':
            S[n - 1 - i] = left
        elif left != right:
            return "NO" 

  
    if n % 2 == 1 and S[n // 2] == '?':
        S[n // 2] = 'a'

    return ''.join(S)

print(solution ("?ab??a"))