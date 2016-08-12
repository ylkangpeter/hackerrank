from util.Util_number import Number

# preprocess for computing
# arr = []
# last_value = [1]
# for i in range(1, 10001):
#     last_value = Number().calc_one(last_value, 2)
#     v=0
#     for i in last_value:
#        v+=i
#     arr.append(v)

arr = [[]] * 10001
max_inx = 0
arr[0] = [1]

group = int(raw_input())
for i in range(group):
    num = int(raw_input())
    if num == 0:
        print 1
    else:

        if max_inx >= num:
            for i in arr[num - 1]:
                result += i
            print result
        else:
            val = arr[max_inx]

            for i in range(max_inx + 1, num + 1):
                val = Number().calc_one(val, 2)
                arr[i] = val
                max_inx += 1
            result = 0
            for i in val:
                result += i
            print result
