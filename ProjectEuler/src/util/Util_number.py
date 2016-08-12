class Number():
    def sum_num(self, a, b):
        if len(b) > len(a):
            tmp = b
            b = a
            a = tmp

        if a == None or len(a) == 0:
            return b
        c = []
        promotion = 0
        i = 0
        for i in xrange(0, len(b)):
            vb = b[i]
            va = a[i]
            total = vb + va + promotion
            if total > 9:
                promotion = 1
                total = total - 10
            else:
                promotion = 0
            c.append(total)

        for j in range(len(a) - len(b), len(a)):
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

    def calc_common(self, a, b):
        if a == 0 or b == 0:
            return 0
        else:
            result = []
            for i in b:
                result.insert(0, 0)
                result = Number.sum_num(self, result, Number.calc_one(self, a, i))
            return result

    # len(b)==1
    def calc_one(self, a, b):
        if a == 0 or b == 0:
            return 0
        else:
            c = []
            promotion = 0
            for i in range(0, len(a)):
                v = b * a[i] + promotion
                promotion = v / 10
                v = v % 10
                c.append( v)
            if promotion != 0:
                c.append(promotion)
            return c


print Number().calc_common(map(int, list(str(234))), map(int, list(str(567))))
