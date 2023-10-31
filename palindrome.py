def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase for case-insensitive comparison
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
