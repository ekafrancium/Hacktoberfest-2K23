def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
