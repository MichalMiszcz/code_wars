
def find_next_square(number):
    return int((number ** (1/2) + 1) ** 2 if (number ** (1/2)).is_integer() else -1)


if __name__ == "__main__":
    print(find_next_square(16))
    print(find_next_square(121))
    print(find_next_square(319225))