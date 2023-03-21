# 30DaysOfPython Day 4
# capitalize count endswith expandtabs find rfind format
# index rindex isalnum isalpha isdecimal isdigit isnumeric
# isidentifier islower isupper join strip replace split 
# title swapcase startswith
print("Thirty" + "Days" + "Of" + "Python")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.swapcase())
print(company[0:1])

print(company.find("Coding"))
print(company.index("Coding"))
print(company.rindex("Coding"))
print(company.replace("Coding", "Python"))
print(company)
first_character = company[0]
last_index = company[len(company) - 1]
tenth_character = company[10]

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies.split(", ")

""" 
Slice out the phrase 'because because because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
"""
sentence = "You cannot end a sentence with because because because is a conjunction"
start_index = sentence.index("because")
end_index = sentence.rindex("because")
because_phrase = sentence[start_index:end_index + len("because")]
print(because_phrase)

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1 +num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2:.2f}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')