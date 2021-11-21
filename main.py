
def kbig(nums,k):
    for i in range(len(nums)):
        lowest_value_index = i
        for z in range(i + 1, len(nums)):
            if nums[z] < nums[lowest_value_index]:
                lowest_value_index = z
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    print(nums[-k])
kbig(nums,k)
