

def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in arr]
        return result

    for i, elem in enumerate(arr):
        p = permutations(arr[:i]+arr[i+1:], n-1)
        for rest in p:
            result.append([elem]+rest)
    return result


def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in arr]
        return result

    for i, elem in enumerate(arr):
        c = combinations(arr[i+1:], n-1)
        for rest in c:
            result.append([elem] + rest)

    return result
l = [1,2,3,4]
print(permutations(l, 3))
print(combinations(l, 3))
