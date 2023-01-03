from itertools import combinations_with_replacement, groupby, combinations, permutations


def itter_grouby(s):
    #Input - 1222311
    #Output - (1, 1) (3, 2) (1, 3) (2, 1)
    s_list = groupby(s)
    for k, c in s_list:
        print(k, len(list(c)))
    # result = []
    # start_s = s[0]
    # j = 1

    # for i in range(1, len(s)):
    #     if s[i] != start_s:
    #         result.append((j, int(s[i-1])))
    #         start_s = s[i]
    #         j = 1
    #         continue
    #     j += 1
    # result.append((j, int(s[-1])))
    # print(*result)

def itter_combwrep(s, n):
    s = ''.join(sorted(s))
    for j in list(combinations_with_replacement(s, int(n))):
        print(''.join(j))

s, n = map(str, input().split())
itter_combwrep(s, n)
itter_grouby(s)
