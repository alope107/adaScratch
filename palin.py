def palindrome(s):
    """This function is going through the index of each
    character and comparing the index of the left hand side to
    the index of the right hand side."""
    for i in range(len(s)): #O(n)
        if s[i] == s[-1 - i]: #O(1)
            return True
        return False

word = "treat"
print(palindrome(word))