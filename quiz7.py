def solution(S):
    i = 0
    patches = 0
    N = len(S)

    while i < N:
        if S[i] == 'X':
            patches += 1
            i += 3  
        else:
            i += 1  
    return patches


print(solution(".X..X")) 