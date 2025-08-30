def heapSort(a):
    def siftDown(start, end):
        root = start
        while root * 2 + 1 < end:
            child = root * 2 + 1
            if child + 1 < end and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    count = len(a)
    start = count // 2 - 1
    end = count
    while end > 1:
        if start >= 0:
            start -= 1
        else:
            end -= 1
            a[end], a[0] = a[0], a[end]
        siftDown(0, end)
    return a

# Example usage:
arr = ["abcv","def","agasgqwegqweg","ascauisoihfoqiwhhofi1qhio2hwifo"]
arr = heapSort(arr)
print("Sorted array is:", arr)
