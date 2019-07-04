# https://leetcode.com/problems/two-sum/

# 1. Restating the problem
# # So I'm going to be adding 2 numbers together in an array to equal the target number. I can't use the same number unless there's a copy of that number in the array and each has one solution. 

# 2. Ask clarifying questions
# # - What if the array has different types? ie str & int
#   - What type of data structure is the array?
#   - Can the answer be a string? Something like "ab" with ["a", "b", ...] in the array?
#   - Any time/space complexity restraints?
#   - Will numbers be null?

# 3. State your assumptions
# # - The values in the array will all be ints
#   - There is exactly one solution
#   - Two values will add up to the target
#   - The same element can't be used twice
#   - The problem is asking for one solution so I'll break as soon as I get a result.

# 4. Think Out Loud
# # 1 - Brainstorm Solutions
#       - My initial thought would be to put all of these into a dictionary so that I could instantly compare to the target. So if the first number it saw was 2 and the target was 9, it would just look for a 7 in that dictionary. Oh but that wouldn't work because I need to return the indexes of the items.
#       - Alright second thought then. I could loop through the array once by adding the complementing number to an empty array. So on the first pass I would a.... Actually scratch this idea. I just thought of a way to make the dictionary work with enumerate. I could just keep track of it like this {num: index}
#   2 - Explain rationale
#       - This dictionary method would be pretty fast because it'd allow us to do constant time lookups. 
#   3 - Discuss Tradeoffs
#       - If there's memory constraints this might not be the best idea
#       - This doesn't have a best case scenario where the two sums are next to or near one             another in the array

#   4 - Suggest improvements
#       - I've spent a bit too much time brainstorming but I think the way you'd do this at the same speed without a dictionary would be to keep another array that kept the complement and then seeing if that number exists in the first?


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[num] = i