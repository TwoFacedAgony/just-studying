def reverse_the_array(data: list) -> list:
    left_pointer = 0
    right_pointer = len(data) - 1

    while left_pointer < right_pointer:
        data[left_pointer], data[right_pointer] = data[right_pointer], data[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return data