def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False

    nums_set = set()
    for num in nums:
        if type(num) == str or num < 0:
            return False
        elif num in nums_set:
            return num
        else:
            nums_set.add(num)

    return False
