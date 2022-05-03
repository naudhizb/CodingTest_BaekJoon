

import sys
#sys.stdin = open("17140_1.txt", "r")

N = 3
R, C, K = list(map(int, input().split()))
TRIM = 100

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

## MAIN

tick = 0
max_tick = 101

def get_count(l):
    cnt = {}
    for i in l:
        if i not in cnt:
            cnt[i] = 0
        cnt[i] += 1
    a = []
    for k in cnt:
        a.append((k, cnt[k]))

    # [[number, count] ...]
    return a

def R_Calc(ll):
    # 1. 등장횟수 오름차순
    # 2. 수가 커지는 순
    ret = []
    for i in ll:
        cnt = get_count(list(filter(lambda x: x!=0, i)))
        cnt.sort(key=lambda x:(x[1], x[0]))
        tmp = [item for sublist in cnt for item in sublist]
        ret.append(tmp)
    len_arr = [len(i) for i in ret]
    max_len = max(len_arr)
    for i in ret:
        while len(i) < max_len:
            i.append(0)
    return ret

# CW
def rotate(ll):
    tmp = zip(*ll[::-1])
    ret = []
    for i in tmp:
        ret.append(list(i))
    return ret
def rev_rotate(ll):
    ll = rotate(ll)
    ll.reverse()
    for i in range(len(ll)):
        ll[i].reverse()
    return ll


def C_Calc(ll):
    ll = rotate(ll)
    ll = R_Calc(ll)
    ll = list(map(list, zip(*ll))) # X Y 전환
    return ll

for i in range(max_tick+1):
    R_len = len(matrix)
    C_len = len(matrix[0])

    # Trim Excessive
    if R_len > TRIM:
        matrix = matrix[:TRIM+1]
        R_len = len(matrix)
    if C_len > TRIM:
        for i in range(R_len):
            matrix[i] = matrix[i][:TRIM+1]
        C_len = len(matrix[0])

    #print(matrix[R-1][C-1])
    #print(*matrix, sep="\n")
    if R <= R_len and C <= C_len:
        if matrix[R-1][C-1] == K:
            break
    if i == max_tick:
        break

    # Check RC Condition
    if R_len >= C_len:
        matrix = R_Calc(matrix)
    else:
        matrix = C_Calc(matrix)

if i == max_tick:
    i = -1

print(i)