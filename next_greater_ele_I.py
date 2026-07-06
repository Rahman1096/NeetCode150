class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hashmap={}
        answer=[-1]*len(nums1)
        for i in range(len(nums2)):
            if not stack or nums2[i]<stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i]>stack[-1]:
                    waiting_num=stack.pop
                    hashmap[waiting_num]=nums2[i]
                stack.append(nums2[i])
        for i in range(len(nums1)):
            answer[i]=hashmap.get(nums1[i],-1)
        return answer    

        