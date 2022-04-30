
import sys
sys.stdin = open("15685.txt","r")

MAX_N = 20+1
MAX_XY = 100+1
MAX_G = 10+1
MAX_D = 3+1  # R U L D
d_curve = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 1 <= N <= 20
# 0 <= x,y <= 100
# 0 <= d <= 3
# 0 <= g <= 10

import copy
def make_dcurve():
    gen0 = [0]
    d_curve.append(gen0)
    for i in range(1, MAX_G):
        prev = copy.deepcopy(d_curve[i-1])
        curr = prev
        for d in prev[::-1]:
            d = (d+1) % MAX_D
            curr.append(d)
        d_curve.append(curr)


n = int(input())
#print(n)

make_dcurve()

a = [[0]*(MAX_XY+1) for _ in range(MAX_XY+1)]
for i in range(n):
    x, y, d, g = map(int, input().split())
    #print(x,y,d,g)
    tmp = list(map(lambda x: (x+d) % MAX_D, d_curve[g]))
    a[y][x] = 1
    for j in tmp:
        x = x+dx[j]
        y = y+dy[j]
        if 0 <= x < MAX_XY and 0 <= y < MAX_XY:
            a[y][x] = 1

answer = 0
for x in range(MAX_XY):
    for y in range(MAX_XY):
        if a[y][x] and a[y][x+1] and a[y+1][x] and a[y+1][x+1]:
            answer += 1


print(answer)
