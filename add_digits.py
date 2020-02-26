def sum_number_digits(number):
    def split_digits(num):
        return [int(x) for x in str(num)]

    def sum_digits(digits):
        return sum(digits)

    while len(str(number)) > 1:
        number = sum_digits(split_digits(number))

    return number
