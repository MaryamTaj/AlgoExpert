def twoNumberSum(array, targetSum):
    # Do not make any assumptions. Consider edge cases:
    # Can you have an empty array? No.
    # Are the integers distinct? Yes.
    # Can multiple pairs add up to the target sum? No.

    # Outline a solution using comments:
    # Start at the first element in the array. Consider its sum with every
    # other element in the array.
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # If you reach the targeted sum, return the first element and the other
            # element in an array. Else, return an empty array.
            if (array[i] + array[j]) == targetSum: return [array[i], array[j]]


    return []

    # Run tests:
# Input: [3,4,-4,8,1,,1,-1,6], targetSum = 10. Output: [11, -1]
# Input: [4,6], targetSum = 10. Output: [4,6]
# Input: [4,6,1], targetSum = 5. Output: [4,1]