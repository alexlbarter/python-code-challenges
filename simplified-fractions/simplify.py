from math import gcd


def simplify(fraction):
    try:
        num, den = [int(x) for x in fraction.split("/")]
    except (AttributeError, ValueError):
        raise ValueError("{} is not a fraction in form 'a/b'".format(fraction))

    if num % den == 0:
        return str(int(num / den))
    else:
        divisor = gcd(num, den)
        return "{}/{}".format(int(num / divisor), int(den / divisor))
