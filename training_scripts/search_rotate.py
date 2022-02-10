nums=[4,5,6,7,0,1,2]
search=int(input("number:"))

if search in nums:
    temp=[]
    index=nums.index(search)
    for j in range(index,len(nums)):
        temp.append(nums[j])
    for i in range(0,index):
        temp.append(nums[i])
    print(temp)
    print(index)
else:
    print("-1")