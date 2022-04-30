

N, M = map(int, input().split())

city = []
house = []
chicken_store = []
chicken_length = 1E+9

for _ in range(N):
    city_line = list(map(int, input().split()))
    city.append(city_line)

for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            house.append([x, y])
        if city[y][x] == 2:
            chicken_store.append([x, y])

from itertools import combinations



