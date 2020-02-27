from math import gcd


def simplify(fraction):
    num, den = [int(x) for x in fraction.split("/")]
    if num % den == 0:
        return str(int(num / den))
    else:
        divisor = gcd(num, den)
        return "{}/{}".format(int(num / divisor), int(den / divisor))
