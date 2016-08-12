from __future__ import print_function


class Test():
    # in this case len(b)<=len(a)
    def sum(self, a, b):
        if a == None or len(a) == 0:
            return b
        c = []
        promotion = 0
        i = 0
        for i in xrange(len(b) - 1, -1, -1):
            vb = b[i]
            va = a[i + len(a) - len(b)]
            total = vb + va + promotion
            if total > 9:
                promotion = 1
                total = total - 10
            else:
                promotion = 0
            c.insert(0, total)

        for j in range(len(a) - len(b) - 1, - 1, -1):
            total = promotion + a[j]
            if total > 9:
                promotion = 1
                total = total - 10
            else:
                promotion = 0
            c.insert(0, total)
        if promotion != 0:
            c.insert(0, 1)
        return c

    def doit(self):
        group = int(raw_input())
        c = []
        for i in xrange(group):
            c = sum(c, map(int, list(raw_input())))

        for i in range(10):
            print(c[i], sep="", end="")
