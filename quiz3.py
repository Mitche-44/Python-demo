from collections import Counter

def even_word(S):
    # Count frequency of each character
    freq = Counter(S)

    deletions = 0

    # If a character appears an odd number of times,
    # we must delete 1 of them to make it even
    for count in freq.values():
        if count % 2 != 0:
            deletions += 1

    return deletions


print(even_word("acbcbba"))   # ➜ 1
print(even_word("axxaxa"))    # ➜ 2
print(even_word("aaaa"))      # ➜ 0
print(even_word(""))          # ➜ 0
print(even_word("abcde"))     # ➜ 5
