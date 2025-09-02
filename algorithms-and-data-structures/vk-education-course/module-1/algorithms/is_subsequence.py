def is_subsequence(*args):
    string, transformed_string = args

    pointer = 0
    for symbol in transformed_string:
        if symbol == string[pointer]:
            pointer += 1
        if pointer == len(string):
            break

    return pointer == len(string)
