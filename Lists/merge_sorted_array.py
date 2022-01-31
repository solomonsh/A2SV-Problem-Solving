class Solution:

    # Approach 1 using sort 
    # Time complexity n log n
    # Space complexity n
    
    def merge(self, nums1, m,nums2, n) -> None:
            if n != 0:
                nums1[m:] = nums2
                nums1.sort()


    # Approach 2 using pointers 
    # Time complexity m + n
    # Space complexity 1
    
    def merge2(self, nums1, m,nums2, n) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        
        print(nums1)

            
        


sol = Solution()


sol.merge2([1,2,3,0,0,0],3,[2,5,6],3)
# sol.merge2([1,0],1,[2],1)
# 