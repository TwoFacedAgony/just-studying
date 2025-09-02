def is_palindrome(num):
    num = str(num)
    pointer = 0
    flag = True
    while pointer <= len(num) // 2:
        if num[pointer] != num[-1 - pointer]:
            flag = False
            break
        pointer += 1

    return flag