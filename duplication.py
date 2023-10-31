def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1

# Example usage
input_nums = list(map(int, input("Enter sorted array elements separated by space: ").split()))
new_length = remove_duplicates(input_nums)
print("New array length after removing duplicates:", new_length)
print("Updated array:", input_nums[:new_length])
