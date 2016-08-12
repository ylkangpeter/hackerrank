# can be optimized. only 250*500+500 numbers need to be calculated. then mirror those values: e.g. a[100][200]=a[200][100]

size = 500
a=[]
for i in range(size):
    a.append([])
    for j in range(size):
        a[i].append(0)

for i in range(size - 1, -1, -1):
    for j in range(size - 1, -1, -1):
        if i == size - 1 or size - 1 == j:
            a[i][j] = 1
        else:
            a[i][j] = (a[i + 1][j] + a[i][j + 1])%1000000007

group = int(raw_input())
for i in range(group):
    line = map(int, raw_input().split(" "))
    m = line[0]
    n = line[1]

    print a[size - 1 - m][size - 1 - n]
