def solution(S, C):
    names = S.split(", ")
    company = C.lower()
    email_count = {}
    result = []

    for full_name in names:
        parts = full_name.strip().split(" ")
        first_initial = parts[0][0].lower()

        if len(parts) == 3:
            middle_initial = parts[1][0].lower()
            last_name = parts[2]
        else:
            middle_initial = ""
            last_name = parts[1]

        last_name_clean = last_name.replace("-", "").lower()[:8]
        email_prefix = first_initial + middle_initial + last_name_clean

        if email_prefix in email_count:
            email_count[email_prefix] += 1
            email = f"{email_prefix}{email_count[email_prefix]}@{company}.com"
        else:
            email_count[email_prefix] = 1
            email = f"{email_prefix}@{company}.com"

        result.append(f"{full_name} <{email}>")

    return ", ".join(result)


# Test
names = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
company = "Example"

print(solution(names, company))
