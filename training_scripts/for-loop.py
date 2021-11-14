import math

print("Loop 1:")
for i in range(7):
    print(str(i))
print("Loop 2:")
for j in range (2,16,2):
    print(str(j))

print("Expense program")

total=0
expenses=[]
num_expenses = int(input("Enter # of expenses you will report: "))
for k in range(num_expenses):
    expenses.append(float(input("Enter " + str(k+1) + ". expense: ")))
total = sum(expenses)
print("Your total expenses: ", total)