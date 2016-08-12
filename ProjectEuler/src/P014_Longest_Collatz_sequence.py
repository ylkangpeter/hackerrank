def calc(num, mydict):
    # print num,

    if num == 1:
        return 0;
    elif num < len(arr) and arr[num] != 0:
        return mydict[num] - 1

    if num % 2 == 0:
        num >>= 1
    else:
        num = num * 3 + 1
    val = 1 + calc(num, mydict)
    if num < len(arr):
        mydict[num] = val
    return val


arr = [0] * 10000000
result = [0] * 5000000

maxV = 1
index = 0
for i in range(1, 5000001):
    vv = calc(i, arr) + 1
    if vv > maxV:
        maxV = vv
        index = i
    result[i - 1] = index

group = int(raw_input())
for i in xrange(group):
    print result[int(raw_input()) - 1]
