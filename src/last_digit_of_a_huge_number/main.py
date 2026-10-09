def last_digit(lst):
    if len(lst) < 1:
        return 1
    elif len(lst) == 1:
        return lst.pop() % 10

    power = lst.pop()

    while len(lst) > 0:
        power = power % 104
        value = lst.pop()
        power = value ** power

    return power % 10


if __name__ == "__main__":
    print(last_digit([]))           # 1
    print(last_digit([123]))        # 3
    print(last_digit([0, 0]))       # 1
    print(last_digit([0, 0, 0]))    # 0
    print(last_digit([1, 2]))       # 1
    print(last_digit([4, 3, 6]))    # 4
    print(last_digit([12, 30, 21])) # 6
    print(last_digit([7, 6, 21]))   # 1
