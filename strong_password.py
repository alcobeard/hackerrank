import re
import timeit

def minimumNumber(n, password):
    count = 0
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count, 6-n)

def minimumNumber2(n, password):
    count = 0
    cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'[!@#$%^&*()\-+]']
    for case in cases:
        if not re.search(case, password):
            count += 1

    return max(count, 6 - n)


def minimumNumber3(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numbers_check = 0
    lower_case_check = 0
    upper_case_check = 0
    special_characters_check = 0

    for i in range(n):
        if numbers_check == 0:
            if (numbers.find(password[i]) != -1):
                numbers_check = 1
        if lower_case_check == 0:
            if (lower_case.find(password[i]) != -1):
                lower_case_check = 1
        if upper_case_check == 0:
            if (upper_case.find(password[i]) != -1):
                upper_case_check = 1
        if special_characters_check == 0:
            if (special_characters.find(password[i]) != -1):
                special_characters_check = 1

    result = 4 - (numbers_check + lower_case_check + upper_case_check + special_characters_check)

    if (n + result) < 6:
        result = 6 - n

    return result

print(timeit.timeit('minimumNumber(33, "#Hacker#RankHackerRank#HackerRank")', globals=globals()))
print(timeit.timeit('minimumNumber2(33, "#HackerRank#HackerRank#HackerRank")', globals=globals()))
print(timeit.timeit('minimumNumber3(33, "#HackerRank#HackerRank#HackerRank")', globals=globals()))