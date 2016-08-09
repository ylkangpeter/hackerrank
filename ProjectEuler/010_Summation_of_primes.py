# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def calc():
    total = 1000000
    primes = []
    for i in xrange(total):
        primes.append(True)

    for i in xrange(2, 1000):
        if primes[i]:
            j = i * i
            round = 1
            while (j < total):
                primes[j] = False
                j += i
                round += 1
    arr = []
    arr.append(0)
    arr.append(0)
    arr.append(2)
    for i in xrange(3, len(primes)):
        if primes[i]:
            arr.append(arr[i - 1] + i)
        else:
            arr.append(arr[i - 1])

    group = int(raw_input())
    for i in range(group):
        N = int(raw_input())

        print arr[N]


calc()