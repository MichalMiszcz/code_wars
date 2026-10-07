from itertools import combinations

def choose_best_sum(t, k, ls):
    combinations_sums = [sum(p) for p in combinations(ls, k)]

    def check_limit(x):
        if x <= t:
            return True
        else:
            return False

    combinations_sums = filter(check_limit, combinations_sums)

    return max(combinations_sums, default=None)


if __name__ == "__main__":
    ts = [50, 55, 56, 57, 58]
    print(choose_best_sum(163, 3, ts)) # 163

    ts = [50]
    print(choose_best_sum(163, 3, ts)) # None

    ts = [91, 74, 73, 85, 73, 81, 87]
    print(choose_best_sum(230, 3, ts)) # 228