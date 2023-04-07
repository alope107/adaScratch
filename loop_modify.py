# A cautionary parable on modifying a list
# as you're doing a for-loop over it

nums = [6, 1, 7, 9, 2, 3, 8]

# # Doesn't work 😥
for num in nums:
    if num > 5:
        nums.remove(num)

print(nums)

# # Also doesn't work 😥
# # for i in range(len(nums)):
# #     if nums[i] > 5:
# #         nums.pop(i)