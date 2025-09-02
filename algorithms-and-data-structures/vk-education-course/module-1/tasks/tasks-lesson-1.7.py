def task():
    N = int(input())
    container_numbers = list(map(int, input().split()))

    answer = -1
    for number in container_numbers:
        if number % 2 == 0:
            answer = number

    return answer
