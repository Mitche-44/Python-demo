def solution(A, F, M):
    N = len(A)
    required_total = M * (N + F)
    known_total = sum(A)
    missing_sum = required_total - known_total

    if missing_sum < F or missing_sum > F * 6:
        return [0]

   
    result = [1] * F
    remaining = missing_sum - F  

    i = 0
    while remaining > 0:
        add = min(5, remaining)
        result[i] += add
        remaining -= add
        i += 1

    return result

print(solution([3, 2, 4, 3], 2, 4)) 