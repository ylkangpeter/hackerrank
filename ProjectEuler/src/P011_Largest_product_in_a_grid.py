# Enter your code here. Read input from STDIN. Print output to STDOUT
arr=[]
size=20
for row in xrange(size):
    arr.append(map(int,raw_input().split(" ")))
    #for col in xrange(size):
     #   arr[row].append(val)

max=0;
for row in xrange(size):
    for col in xrange(size):
        #right
        if col<size-3:
            val=arr[row][col]*arr[row][col+1]*arr[row][col+2]*arr[row][col+3]
            if val>max:
                max=val
        #down
        if row<size-3:
            val=arr[row][col]*arr[row+1][col]*arr[row+2][col]*arr[row+3][col]
            if val>max:
                max=val
        #right down
        if row<size-3 and col<size-3:
            val=arr[row][col]*arr[row+1][col+1]*arr[row+2][col+2]*arr[row+3][col+3]
            if val>max:
                max=val
        #left down
        if row<size-3 and col>=3:
            val=arr[row][col]*arr[row+1][col-1]*arr[row+2][col-2]*arr[row+3][col-3]
            if val>max:
                max=val
print max