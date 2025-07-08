from itertools import combinations

# Helper function: checks if a string has all unique characters
def has_unique_chars(s):
    return len(set(s)) == len(s)

# Main solution function
def solution(A):
    max_length = 0  # to track the longest valid string length

    # Try all combinations of 1 to len(A) strings
    for r in range(1, len(A) + 1):
        for combo in combinations(A, r):
            joined = ''.join(combo)  # concatenate strings in combo
            if has_unique_chars(joined):
                max_length = max(max_length, len(joined))

    return max_length

#  Sample Test Cases
if __name__ == "__main__":
    print(solution(["co", "dil", "ity"]))                     # ➜ 5
    print(solution(["abc", "yyy", "def", "csv"]))            # ➜ 6
    print(solution(["potato", "kayak", "banana", "racecar"])) # ➜ 0
    print(solution(["eva", "jqw", "tyn", "jan"]))            # ➜ 9
