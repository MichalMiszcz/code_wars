from collections import Counter

def count_chars(s):
    s = list(filter(str.islower, s))
    return Counter(s)

def sort_list(l):
    l.sort()
    l.sort(key=lambda x: len(x), reverse=True)

def mix(s1, s2):
    chars_counted_s1 = count_chars(s1)
    chars_counted_s2 = count_chars(s2)

    chars_counted_s1_s2 = {k: (chars_counted_s1.get(k, 0), chars_counted_s2.get(k, 0)) for k in sorted(chars_counted_s1.keys() | chars_counted_s2.keys())}

    greater_list = []
    for c, tup in chars_counted_s1_s2.items():
        if max(tup[0], tup[1]) > 1:
            if tup[0] == tup[1]:
                greater_list.append('=:' + c * tup[0])

            if tup[0] > tup[1]:
                greater_list.append('1:' + c * tup[0])

            if tup[0] < tup[1]:
                greater_list.append('2:' + c * tup[1])

    sort_list(greater_list)

    return '/'.join(greater_list)




if __name__ == "__main__":
    print(mix("Are they here", "yes, they are here"))
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacsaa","MynwdKizfd$lvse+gnbaGydxyXzaypaa"))