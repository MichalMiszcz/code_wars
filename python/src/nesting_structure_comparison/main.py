def len_of_list(my_list):
    len_of_my_list = len(my_list)

    my_list_structure = []
    for element in my_list:
        if type(element) == list:
            my_list_structure.append(len_of_list(element))
        else:
            my_list_structure.append(len_of_my_list)

    return my_list_structure

def same_structure_as(original, other) -> bool:
    if type(original) == list and type(other) == list:
        return len_of_list(original) == len_of_list(other)
    elif type(original) == type(other):
        return True

    return False


if __name__ == '__main__':
    print(same_structure_as(1,2))
    print(same_structure_as([[], []],[[], []]))
    print(same_structure_as([1,[1,1]],[2,[2,2]]))
    print(same_structure_as([[1,1], 1],[2,[2,2]]))