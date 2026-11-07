from sympy.utilities.iterables import multiset_permutations

def permutations(s):
    output = [''.join(p) for p in list(multiset_permutations(s))]
    return output

if __name__ == '__main__':
    print(permutations('ab'))
    print(permutations('aabb'))