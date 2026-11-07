
def digital_root(number):
    digits_sum = sum(int(n) for n in str(number))
    return digits_sum if len(str(digits_sum)) == 1 else digital_root(digits_sum)

if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(9425))