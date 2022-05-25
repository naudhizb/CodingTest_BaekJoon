array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    print("Quick Sort[{} {}]".format(start, end))
    print(array[start:end+1])
    if start >= end:
        print("Return with nothing")
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        print("Loop [{} {}] Pivot:{}".format(left, right, array[pivot]))
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1
        if left > right : # sorted. except array[right]
            # array는 pivot에 의하여 정렬되었으나, pivot의 위치가 정확히 들어가있지 않음.
            # array[right] 의 위치가 pivot보다 작은 첫번째 데이터이므로 pivot과 교체
            print("Pivot Swap {}[{} {}]".format(pivot, left, right))
            print(array[start:end+1])            
            array[right], array[pivot] = array[pivot], array[right]
            print(array[start:end+1])            
        else : # need swap
            print("Data Swap {}[{} {}]".format(pivot, left, right))
            print(array[start:end+1])                        
            array[left], array[right] = array[right], array[left]
            print(array[start:end+1])            
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

res = sorted(array)

print(res)

array.sort()
print(array)