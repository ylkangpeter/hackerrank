__author__ = 'peter'


def calc(num):
    # >9 billion, >6 million, >3 thousand
    if num == 0:
        return "Zero"
    result = ""
    if num > 1000000000:
        billion_part = num / 1000000000
        result = result + sub(billion_part).strip() + " Billion "
        num = num % 1000000000
    if num > 1000000:
        million_part = num / 1000000
        result = result + sub(million_part).strip() + " Million "
        num = num % 1000000
    if num > 1000:
        thousand_part = num / 1000
        result = result + sub(thousand_part).strip() + " Thousand "
        num = num % 1000
    result += sub(num)
    return result.strip()


# where num<1000
def sub(num):
    if num == 0:
        return
    result = ""
    if num >= 100:
        hundreds = num / 100
        result += mods[hundreds] + " Hundred "
        num = num % 100
    if num < 20:
        result += mods[num]
    else:
        inx = num / 10
        result += tens[inx] + " "
        num = num % 10
        if num > 0:
            result += mods[num]
    return result


mods = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

groups = int(raw_input())
for i in range(groups):
    val = int(raw_input())
    print calc(val)
