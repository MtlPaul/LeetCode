# Two Sum Problem 
# Time complexity : O(n). We traverse the list containing nnn elements only once. Each look up in the table costs only O(1) time.
# Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.


def twoSum(self, nums, target):
    index = {}
    for i, x in enumerate(nums):
        if target - x in index:
            return [index[target - x], i]
        index[x] = i