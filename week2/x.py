def nextGreaterElement(nums1, nums2 ):
    nums1Index = {n:i for i,n in enumerate(nums1)}
    ans = [-1]*len(nums1)
    for i in range(len(nums2)):
        if nums2[i] not in nums1:
            continue
        for j in range(i+1, len(nums2)):
             if nums2[j] > nums2[i]:
                 inx = nums1Index[nums2[i]]
                 ans[inx] = nums2[j]
                 break
    print(ans)


nextGreaterElement([4,1,2], [1,3,4,2])
