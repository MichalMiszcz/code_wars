from math import prod


def persistent(number):
    iterations = 0
    while len(str(number)) > 1:
        digits_prod = prod(int(n) for n in str(number))
        number = digits_prod
        iterations += 1
    return iterations

if __name__ == "__main__":
    print(persistent(39))
    print(persistent(9425))
    print(persistent(4))