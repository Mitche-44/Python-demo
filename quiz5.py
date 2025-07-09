def solution(S):
    total_x = S.count('x')
    total_y = S.count('y')

    left_x = left_y = 0
    count = 0

    for i in range(1, len(S)):  
        if S[i - 1] == 'x':
            left_x += 1
        elif S[i - 1] == 'y':
            left_y += 1

        right_x = total_x - left_x
        right_y = total_y - left_y

        if left_x == left_y or right_x == right_y:
            count += 1

    return count

print(solution("ayxbx"))  