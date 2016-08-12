from P010_Summation_of_primes import Primes

primes = Primes().genPrimes(60000)


def calc():
    groups = int(raw_input())
    for i in xrange(groups):
        num = int(raw_input())
        do_it(num)


# have to use cache (mydict)
def do_it(num, primes, mydict):
    group = 0
    total = 1
    while total <= num:
        group += 1
        total = 1
        n1 = 0
        n2 = 0

        if group % 2 == 0:
            n1 = group / 2
            n2 = group + 1
        else:
            n1 = (group + 1) / 2
            n2 = group

        if mydict.get(n1) != None:
            total *= mydict.get(n1)
        else:
            inx = 0
            total1 = 1
            tmp=n1
            while n1 != 1 and n1 >= primes[inx]:
                cur = 1
                while n1 % primes[inx] == 0:
                    cur += 1
                    n1 = n1 / primes[inx]
                total1 *= cur
                inx += 1
            total *= total1
            mydict[tmp] = total1

        if mydict.get(n2) != None:
            total *= mydict.get(n2)
        else:
            inx = 0
            total2 = 1
            tmp=n2
            while n2 != 1 and n2 >= primes[inx]:
                cur = 1
                while n2 % primes[inx] == 0:
                    cur += 1
                    n2 = n2 / primes[inx]
                total2 *= cur
                inx += 1
            total *= total2
            mydict[tmp] = total2
    print group * (group + 1) / 2



def genPrimes(self, total):
    primes = []
    for i in xrange(total):
        primes.append(True)

    for i in xrange(2, 100):
        if primes[i]:
            j = i * i
            round = 1
            while (j < total):
                primes[j] = False
                j += i
                round += 1
    arr = []
    for i in xrange(2, len(primes)):
        if primes[i]:
            arr.append(i)
    return arr