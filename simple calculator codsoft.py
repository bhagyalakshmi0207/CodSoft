def cal():
        print("Simple Calculator")   
    
num1=int(input("Enter first no:"))
num2=int(input("Enter second no:"))

print("Simple Calculator:")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")

operation=input("Enter operation(1/2/3/4):")

if operation=="1":
        print("The result is:", num1 + num2)
elif operation=="2":
        print("The result is:", num1 - num2)
elif operation=="3":
        print("The result is:", num1 * num2)
elif operation=="4":
        print("The result is:", num1 / num2)    
    
else:
        print("Invalid")