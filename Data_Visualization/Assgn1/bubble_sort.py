def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else :
                # Set the flag to False to end the loop
                swapped = False


# Verify it works
random_list_of_nums = [5, 4, 2]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)