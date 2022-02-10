
def removeDubs(nums):
    tempnums=[]
    if len(nums)==0:
        print("list is empty")
    else:
        for i in range(0,len(nums)):
            if not nums[i] in tempnums: 
                tempnums.append(nums[i])
        print(tempnums)
        print(len(tempnums))

def sortingNums(nums):
    temp=0
    for i in range (0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]>nums[j]:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
            #print(nums)
    return nums
nums1=[0,3,2,5,7,0,3,3,9,1,1,1,2]

result=sortingNums(nums1)
removeDubs(result)
