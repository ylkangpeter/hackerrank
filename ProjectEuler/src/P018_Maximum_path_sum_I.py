__author__ = 'ylkang'

groups = int(raw_input())
for i in range(groups):
    lines = int(raw_input())
    arr = [] * lines
    for j in range(lines):
        row = map(int, raw_input().split(" "))
        arr.append(row)
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            val = 0
            if x > 0:
                if y > 0:
                    val = arr[x - 1][y - 1]
                if y < len(arr[x - 1]):
                    val = max(arr[x - 1][y], val)
            arr[x][y] = arr[x][y] + val
    result = 0
    for x in arr[lines - 1]:
        if x > result:
            result = x
    print result
