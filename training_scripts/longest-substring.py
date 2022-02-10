problem=input("Enter your string:")

longest=0
ch=""
ch_longest=""
for i in range (0,len(problem)-1):
    ch = ""+problem[i]
    templong=len(ch)
    for j in range (i+1,len(problem)):
        if not problem[j] in ch:
            if j<len(problem)-1:
                ch = ch+problem[j]
                templong=len(ch)
            elif j==len(problem)-1 and templong>longest:
                longest=templong
                ch_longest=ch 
        else:
            if templong > longest:
                longest=templong
                ch_longest=ch
            break
print("longest substring: " + ch_longest)
print("lenght of longest substring: ", longest)
