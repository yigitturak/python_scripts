def reverseString(str_num):
    new_num=""
    last_index=len(str_num)-1
    for i in range(0,len(str_num)):
        new_num+=str_num[last_index-i]

    return new_num

str_num=input("enter number:")
if str_num[0] == "-":
    print("-" + reverseString(str_num[1:]))
else:
    print(reverseString(str_num))