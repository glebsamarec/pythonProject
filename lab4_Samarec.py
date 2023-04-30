#Task 1
print('Task 1')
n = int(input("Enter a number: "))
print(n >= 100)
#Task 2
print('Task 2')
n = float(input("Enter first number : "))

m = float(input("Enter a second number: "))

if n > m:
    print("First number > Second")
elif n < m:
    print("First number < Second")
else:
    print("First number = Second")
#Task 3
print('Task 3')
flower = input("Enter flower name: ")

if (flower == 'Spathiphyllum'):
    print("“Yes - Spathiphyllum is the best plant ever!”")
elif(flower == "spathiphyllum"):
    print('No, I want a big Spathiphyllum!')
else:
    print('Spathiphyllum! Not \t' + flower + '!')
#Task 4
print('Task 4')
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = round(income * 0.18 - 556.02)
else:
    tax = round(14839.02 + 0.32 * (income - 85528))

if tax < 0:
    tax = 0
print(f"The tax is: {tax:.1f} tallers")