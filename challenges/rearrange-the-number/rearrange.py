def rearrange(number):
    max_num = int("".join(sorted([x for x in str(number)], reverse=True)))
    min_num = int("".join(sorted([x for x in str(number)])))
    return max_num - min_num
