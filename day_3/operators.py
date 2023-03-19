# 30 days of Python Day 3
age = 25
height = 167.9
complex_number = 3 + 4j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("Area:", area)

side_a = input("Enter first side of the triangle: ")
side_b = input("Enter second side of the triangle: ")
side_c = input("Enter third side of the triangle: ")
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

print(len("python") != len("dragon"))
print("jargon" in "I hope this course is not full of jargon")
print("on" not in "python" and "on" not in "dragon")
length = len("python")
print("length", length, "float", float(length), "string", str(length))

number = int(input("Enter a number: "))
print("number is even") if number % 2 == 0 else print("number is odd")

print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int("9.8") == 10)

hours = int(input("Enter hours: "))
rph = int(input("Enter rate/hour: "))
print("Your weekly earning is", hours * rph)

years = int(input("Enter number of years you have lived: "))
print("You have lived for", years ** 365 * 24 * 3600, seconds)

# from day 1 to day 3, there's no mentioned of loop,but here we are
# to display this table with a script
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1:
            print(i, end=" ")
        elif j == 2:
            print(1, end=" ")
        elif j == 3:
            print(i**2, end=" ")
        elif j == 4:
            print(i**3, end=" ")
        else:
            print(i**4, end=" ")
    print()