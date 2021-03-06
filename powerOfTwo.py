'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
Code By Saideep Shetty
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n > 2:
                n = n /2
            
            if n == 2:
                return True
            else:
                return False
