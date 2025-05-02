# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    # Base case: when either number is 0, return 0 (no further digits to compare)
    if apples == 0 and oranges == 0:
        return 1
    
    if apples == 0 or oranges == 0:
        return 0
    
    # Compare the last digits of both numbers
    match = 1 if apples % 10 == oranges % 10 else 0
    
    if apples < 10 and oranges < 10:
        return match
    
    # Recursively compare the remaining digits
    return match + digit_match(apples // 10, oranges // 10)


