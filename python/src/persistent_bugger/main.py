from math import prod


def persistence(number):
    iterations = 0
    while len(str(number)) > 1:
        digits_prod = prod(int(n) for n in str(number))
        number = digits_prod
        iterations += 1
    return iterations

if __name__ == "__main__":
    print(persistence(39))
    print(persistence(999))
    print(persistence(4))