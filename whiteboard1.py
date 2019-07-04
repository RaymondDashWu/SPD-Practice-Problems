# Given n numbers find if it has duplicates

# Clarifying question: Do I return the duplicates themselves or if the array has duplicates (boolean)?
# Answer: return duplicates OK

# Clarifying question: Do I return all duplicates or just the first one?
# Answer: all of them OK

# Assumptions:
# - Arrays will have at least one duplicate OK
# - No time/space constraints OK

# PSEUDO BRAINSTORM
# initialize with prev variable
# loop over a sorted version of the list O(n*logn)
# check if prev in result
# if not then add to result

# Example Outputs OK
# [1, 1, 2] returns [1]
# [1, 1, 2, 2, 8, 8, 9] returns [1, 2, 8]
# [1, 1, 1, 1] returns [1]

def find_dupes(list):
    result = []
    prev = None
    list.sort()
    for num in list:
        if list[prev] == list[num]:
            if prev not in result:
                list.append(prev)
            else:
                prev = num

