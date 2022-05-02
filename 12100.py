'''
2048 게임의 핵심 중의 하나는 방향키를 움직였을 때 숫자가 합쳐지는 부분입니다.
해당 부분을 reduce 함수로 분리하고, In/Out을 먼저 정의합니다.

reduce 함수는 N길이의 l을 입력으로 받고,
N길이의 리스트를 반환합니다.
내부 동작으로 숫자들을 한쪽에 모아 합친 뒤 반환하며
반환값은 N길이의 리스트를 반환합니다.

그 뒤로 mv_up/down/left/right함수를 작성하고
최종으로 함수를 활용하기위하여 DFS 를 작성하여 동작시킵니다.

Depth는 문제에서 정의한 대로 5로 구현됩니다.
'''

import sys

# sys.stdin = open("12100.txt", "r")
input = sys.stdin.readline

N = int(input())
MAX_DEPTH = 5

value_max = 0

matrix = []
for i in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)


def reduce(l, isright=False):
    last_digit = 0
    ret = []
    tmp = list(filter(lambda x: x != 0, l))
    if isright: tmp.reverse()
    for i in tmp:
        if last_digit == i:
            ret.pop()
            ret.append(2*i)
            last_digit = 0
        else:
            last_digit = i
            ret.append(i)
    if isright: ret.reverse()
    if not isright:
        ret = ret + [0] * (len(l)-len(ret))
    else:
        ret = [0] * (len(l) - len(ret)) + ret
    return ret

#ref : https://choichumji.tistory.com/74
def rotate(arr):
    cw = -1
    lot = zip(*arr[::cw])
    ret = [list(elem) for elem in lot]
    return ret

def mv_left (mat):
    nmat = []
    for y in range(N):
        nmat.append(reduce(mat[y]))
    return nmat

def mv_right (mat):
    nmat = []
    for y in range(N):
        nmat.append(reduce(mat[y], True))
    return nmat

def mv_up(mat):
    nmat = rotate(mat)
    nmat = mv_right(nmat)
    nmat = rotate(nmat)
    nmat = rotate(nmat)
    nmat = rotate(nmat)
    return nmat

def mv_down(mat):
    nmat = rotate(mat)
    nmat = rotate(nmat)
    nmat = rotate(nmat)
    nmat = mv_right(nmat)
    nmat = rotate(nmat)
    return nmat

def DFS(mat, i):
    if i == MAX_DEPTH:
        for y in range(N):
            for x in range(N):
                global value_max
                value_max = max(value_max, mat[y][x])
        return

    DFS(mv_down(mat), i+1)
    DFS(mv_up(mat), i + 1)
    DFS(mv_left(mat), i + 1)
    DFS(mv_right(mat), i + 1)
    return


# input Test
# print(N)
# print(matrix)

# Unit Test for Reduce
# print(reduce([2, 0, 2, 4, 4, 8, 2, 2, 2, 2, 2], False))
# print(reduce([2, 0, 2, 4, 4, 8, 2, 2, 2, 2, 2], True))

#mv test
# print(mv_left(matrix))
# print(mv_right(matrix))
# t = rotate(matrix)
#
# print(*t, sep='\n')
# print(*mv_up(t), sep='\n')
#
# print(*t, sep='\n')
# print(*mv_down(t), sep='\n')


# DFS TEST

DFS(matrix, 0)
print(value_max)