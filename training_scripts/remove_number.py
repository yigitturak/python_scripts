nums=[0,3,2,5,7,0,3,3,9,1,1,1,2]
loop=True
remove=int(input("give your number what you want to remove:"))
while(loop):
    if remove in nums:
        nums.remove(remove)
    else:
        loop=False
print(nums)
print(len(nums))