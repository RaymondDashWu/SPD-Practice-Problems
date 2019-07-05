def is_isogram(string):
    letter_checker_dict = {}
    for letter in string.lower():
        if letter.isalnum() and letter in letter_checker_dict:
            return False
        else:
            letter_checker_dict[letter] = 1
    return True