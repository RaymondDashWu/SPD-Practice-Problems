# https://leetcode.com/problems/reverse-integer/

# 1. Restating the problem
# # Reverse the digits of a number. Emphasis on digits because it can be a negative symbol too.

# 2. Ask clarifying questions
#   - Why does the 32 bit signed matter? What will this be used for?
#   - Any time/space constraints?

# 3. State your assumptions
#   - No further assumptions than what was given

# 4. Think Out Loud
# # 1 - Brainstorm Solutions
#       - I think converting it to a string first might be a good start. That way I can iterate through each digit. I would imagine first checking if that character is a digit. If it is, add it to a reversed string variable. Otherwise put it in the front? At this moment I think a negative is the only symbol that you can get. However, I'll leave a blank variable just in case.
#   2 - Explain rationale
#       - Doing it this way would allow me to easily and quickly reverse that number. I just have to add a check to make sure it's 32 bit.
#   3 - Discuss Tradeoffs
#       - O(n) space and time complexity. I think that the powe(2,31) check I added is nice as it allows you to easily change it if we wanted to switch to, say, an 8 bit signed integer.

#   4 - Suggest improvements
#       - Nothing immediately comes to mind. Unless there's a built in python function that does this or something similar to it. Syntactically I'm sure I could make it simpler, especially with list comprehension. However, this makes sense to me.

class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = ""
        has_neg = ""
        for character in str(num)[::-1]:
            if character.isdigit():
                reversed_num += character
            else:
                has_neg += character
        if abs(int(has_neg + reversed_num)) < pow(2,31):
            return int(has_neg + reversed_num)
        else:
            return 0