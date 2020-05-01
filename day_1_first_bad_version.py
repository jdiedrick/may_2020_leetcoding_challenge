# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while start <= end:
            mid = (start + end) // 2
            first_guess = isBadVersion(mid)
            second_guess = isBadVersion(mid + 1)
            if (first_guess == False) and (second_guess == True):
                return mid + 1
            if first_guess == True:
                end = mid
            else:
                start = mid
