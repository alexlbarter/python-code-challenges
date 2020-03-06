from math import gcd


def is_primitive(num_list):
    a, b, c = sorted(num_list)
    # Check if Pythagorean triple
    if a ** 2 + b ** 2 == c ** 2:
        pass
    else:
        return False

    # Check if primitive
    for pair in ((a, b), (a, c), (b, c)):
        if gcd(pair[0], pair[1]) == 1:
            continue
        else:
            return False
    else:
        return True
