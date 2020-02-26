def sum_number_digits(number):
    try:
        if number < 0:
            raise ValueError("{} is not positive")
        if number % 1 != 0:
            raise ValueError("{} is not an integer")
    except TypeError:
        raise ValueError("{} is not a number")

    def split_digits(num):
        return [int(x) for x in str(num)]

    def sum_digits(digits):
        return sum(digits)

    while len(str(number)) > 1:
        number = sum_digits(split_digits(number))

    return number