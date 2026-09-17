class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_lower=s.lower()
        new_string=""
        for char in string_lower:
            if char.isalnum():
                new_string+=char
        return new_string==new_string[::-1] 