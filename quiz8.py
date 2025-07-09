def solution(A):
    A.sort()
    rooms = 0
    count = 0

    for i in range(len(A)):
        count += 1
        if count == A[i]:
            rooms += 1
            count = 0

    return rooms

print(solution([1, 1, 1, 1, 1]))  