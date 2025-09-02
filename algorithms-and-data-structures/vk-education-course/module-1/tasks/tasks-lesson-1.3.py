def task_1():
    scores = list(map(int, input().split(' ')))
    answer = list(filter(lambda x: x > 0, scores)) + [0] * scores.count(0)
    print(*answer)

def task_2():
    N = int(input())
    results = list(map(int, input().split(' ')))
    element = int(input())
    print(*list(filter(lambda x: x != element, results)))
