# Input numbers

num1 = int(input("input first number "))
num2 = int(input("input second number "))
op   = (input("input operation "))

# If statements

if op == "+" :
    answer = num1 + num2 
elif op == "-" :
    answer = num1 - num2 
elif op == "/" :
    answer = num1 / num2 
elif op == "*" :
    answer = num1 * num2 
else: 
    print("You haven't picked and arithmetic op")

print( num1, "  ", op, " ", num2, " = ", answer)
