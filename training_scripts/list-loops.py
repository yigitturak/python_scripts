acronyms = ['LOL', 'IDK', 'SMH', 'AFAIK']
print(acronyms)
acronyms.append('BTW')
print(acronyms)
acronyms.remove('SMH')
print(acronyms)

word1 = "LOL"
word2 = "SMH"
if word1 in acronyms:
    print("True")
if word2 in acronyms:
    print ("True")
else:
    print("False")

for acronym in acronyms:
    print(acronym)

expenses=[10.50, 8, 23, 4.75, 17]
sum1 = 0
for x in expenses:
    sum1 +=x

print("Total spent $",sum1, " today")
print("Total spent $",sum1, " today",sep='') # sep is removing the default space before adding sum1

sum2 = sum(expenses) # with this, don't need to use for loop as above
print("Total spent $",sum2, " today",sep='') # sep is removing the default space before adding sum2
