# def find_duplicate(nums):
#     if not nums or isinstance(nums, str):
#         return False
#     if len(nums) < 2:
#         return False
#     if any(num < 0 for num in nums):
#         return False

#     nums_set = set()
#     for num in nums:
#         if num in nums_set:
#             return num
#         else:
#             nums_set.add(num)

#     return False
