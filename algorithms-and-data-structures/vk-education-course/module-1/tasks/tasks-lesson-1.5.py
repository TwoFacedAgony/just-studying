from math import inf


def task():
    N = int(input())
    results = list(map(int, input().split()))
    min_difference = inf
    nums = [None, None]
    for i in range(N - 1):
        if abs(results[i] - results[i + 1]) < min_difference:
            min_difference = abs(results[i] - results[i + 1])
            nums = [results[i], results[i + 1]]
    print(*nums)