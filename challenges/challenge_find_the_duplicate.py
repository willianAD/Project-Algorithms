# def find_duplicate(nums):
#     if nums is None:
#         return False
#     if isinstance(nums, str):
#         return False
#     if not isinstance(nums, list) or len(nums) <= 1:
#         return False
#     if any(num < 0 for num in nums):
#         return False

#     nums_set = set()
#     for num in nums:
#         if num in nums_set:
#             return num
#         nums_set.add(num)

#     return False
