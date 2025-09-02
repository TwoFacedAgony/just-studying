from typing import Any


def two_sum_for_sorted(nums: list[int], target: int) -> tuple[int, int | Any] | None:
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer != right_pointer:
        if nums[left_pointer] + nums[right_pointer] - target == 0:
            return left_pointer, right_pointer
        elif nums[left_pointer] + nums[right_pointer] - target < 0:
            left_pointer += 1
        else:
            right_pointer -= 1
    return None


