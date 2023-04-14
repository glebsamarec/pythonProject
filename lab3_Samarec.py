#Task1
print("Task 1")
import math
def gaussian(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(math.pow(x - mu, 2) / (2 * math.pow(sigma, 2))))
x = 1.5
mu = 0
sigma = 1
result = gaussian(x, mu, sigma)
print(result)
#Task2
print("Task 2")
john, mary, adam = 3, 5, 6
print(str(john) + ',' + str(mary) + ',' + str(adam))
totalApple = john + mary + adam
print(totalApple)
print("Загальна кількість: " + str(totalApple) + "яблук")
#Task3
print("Task 3")
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers / 1.60934

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#Task4/1
print("Task 4/1")
x1 = 0
x2 = 1
x3 = -1

y1 = 3*x1**3 - 2*x1**2 + 3**x1 - 1
y2 = 3*x2**3 - 2*x2**2 + 3**x2 - 1
y3 = 3*x3**3 - 2*x3**2 + 3**x3 - 1

print("Результаты:")
print("При x = 0, y =", y1)
print("При x = 1, y =", y2)
print("При x = -1, y =", y3)
#Task4/2
print("Task 4/2")
x1 = 0
x2 = 1
x3 = -1

y1 = (3*x1**3 - 2*x1**2 + 3**x1 - 1)
y2 = (3*x2**3 - 2*x2**2 + 3**x2 - 1)
y3 = (3*x3**3 - 2*x3**2 + 3**x3 - 1)

print("Результати:")
print("При x = 0, y =", y1)
print("При x = 1, y =", y2)
print("При x = -1, y =", y3)
#Task5
print("Task 5")
a = 2
seconds = 3600
print("Hours: ", a)
print("Hours: ", a * seconds)
#Task6
print("Task 6")
a = 2.0
b = 0.0  # input a float value for variable b here

print(a + b)  # output the result of addition here
print(a - b)  # output the result of subtraction here
print(a * b)  # output the result of multiplication here

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")

print("\nThat's all, folks!")
#Task7
print("Task 7")
x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x))))

print("y =", y)
#Task8
print("Task 8")
while True:
    while True:
        try:
            hour = int(input("Starting time (hours): "))
            if hour > 23:
                print("Помилка, не вірно вказаний час!")

            else:
                break
        except ValueError as e:

            pass

    while True:
        try:
            mins = int(input("Starting time (minutes): "))
            if mins > 59:
                print("Помилка, не вірно вказаний час!")
            else:
                break
        except ValueError as e:
            pass

    while True:
        try:
            dura = int(input("Event duration (minutes): "))
            break
        except ValueError as e:
            pass

    total_start_minutes = hour * 60 + mins
    total_end_minutes = total_start_minutes + dura

    end_hour = total_end_minutes // 60 % 24
    end_minute = total_end_minutes % 60
    print(f"Закінчення: {end_hour:02d}:{end_minute:02d}")

    while True:
        user_input = input("Бажаєте продовжити? (так/ні): ")
        if user_input.lower() == "ні":
            break
        elif user_input.lower() == "так":
            break
        else:
            print("Некоректний ввод. Введіть 'так' або 'ні'.")

    if user_input.lower() == "ні":
        break