# Day 2: 30 Days of python programming
# EX1
first_name = "Minh"
last_name = "Truong"
full_name = "Minh Truong"
country = "United States"
city = "Denver"
age = 25
year = 2023
is_married = True
is_true = True
is_light_on = False
number_of_pets, pets_name, is_fed = 5, ["Tuco", "buba", "meany", "sakura"], False

# EX2
print("first_name", type(first_name))
print("last_name", type(last_name))
print("full_name", type(full_name))
print("country", type(country))
print("city", type(city))
print("age", type(age))
print("year", type(year))
print("is_married", type(is_married))
print("is_true", type(is_true))
print("is_light_on", type(is_light_on))
print("number_of_pets", type(number_of_pets))
print("pets_name", type(pets_name))
print("is_fed", type(is_fed))

print(len(first_name))

print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
pi = 3.14
area_of_circle = pi*radius**2
circum_of_circle = 2*pi*radius
print(area_of_circle, circum_of_circle)
input_radius = int(input("What's the circle's radius?"))
print("area", pi*input_radius**2)

input_first_name = input("What's your first name?")
input_last_name = input("What's your last name?")
input_country = input("What's your country?")
input_age = input("What's your age?")
user = {input_first_name, input_last_name, input_country, input_age}
print("user", user)
