// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m + n
        i = 0
        while i < total and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[total-i-1] = nums2[n-1]
                n -= 1
            else:
                nums1[total-i-1] = nums1[m-1]
                m -= 1
            i += 1
            # print(nums1,m,n)
        if m < 0:
            nums1[:-m] = nums2[:-m]
        