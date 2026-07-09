
def narcissistic(number):
    return number == sum(int(n) ** len(str(number)) for n in str(number))

if __name__ == "__main__":
    print(narcissistic(153))
    print(narcissistic(1652))