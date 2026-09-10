num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

largestNum = None

if num1 > num2 and num1 > num3:
    largestNum = num1
elif num2 > num1 and num2 > num3:
    largestNum = num2
else:
    largestNum = num3
print(largestNum)