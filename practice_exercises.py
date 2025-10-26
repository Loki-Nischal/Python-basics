# write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd.
def lesser_greater(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)
    
result = lesser_greater(5, 8)
print(result)  # Output: 8

# write a function that takes a two-word string and returns True if both words begin with the same letter
def same_starting_letter(two_word_string):
    words = two_word_string
    if len(words) != 2:
        return False  # Not a two-word string
    if words[0][0].lower() == words[1][0].lower():
        return True
    
result1 = same_starting_letter("Hi  Hero")
print(result1)  # Output: True
  