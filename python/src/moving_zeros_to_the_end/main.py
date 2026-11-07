def move_zeros(lst):
    final_lst = [n for n in lst if n != 0]
    zeros = [n for n in lst if n == 0]
    final_lst.extend(zeros)
    return final_lst


if __name__ == '__main__':
    lst = [1, 2, 0, 3, 0, 4, 5]
    print(move_zeros(lst))