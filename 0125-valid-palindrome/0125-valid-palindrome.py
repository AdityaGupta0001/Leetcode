class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        new_str = ''
        for i in s:
            if i in alphanum:
                new_str+=i
        
        if new_str.lower() == new_str[::-1].lower():
            return True
        else:
            return False