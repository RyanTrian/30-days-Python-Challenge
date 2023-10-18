# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# # Print the lists and its length
# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Countries:', countries)
# print('Number of countries:', len(countries))

# lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
# print('different data types:', lst)

# ------------------------------ Unpacking List ------------------------------ #
# First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits 
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']
# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10
# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr)
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)

# # ------------------------- Slicing Items from a List ------------------------ #
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:4] # it returns all the fruits
# # this will also give the same result as the one above
# all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
# orange_and_mango = fruits[1:3] # it does not include the first index
# orange_mango_lemon = fruits[1:]
# orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[-4:] # it returns all the fruits
# orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
# orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
# reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

# # -------------------------- Adding Items to a List -------------------------- #
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banana' in fruits
# print(does_exist)  # True
# does_exist = 'lime' in fruits
# print(does_exist)  # False

# -------------------------- Adding Items to a List -------------------------- #
# syntax
# lst = list()
# lst.append(item)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
# print(fruits)

# ------------------------ Inserting Items into a List ----------------------- #
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2, 'apple') # insert apple between orange and mango
# print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
# print(fruits)

# ------------------------ Removing Items from a List ------------------------ #
# syntax
# lst = ['item1', 'item2']
# lst.remove(item)

# ------------------------- Removing Items Using Pop ------------------------- #
# The pop() method removes the specified index, (or the last item if index is not specified):

# syntax

# lst = ['item1', 'item2']
# lst.pop()       # last item
# lst.pop(index)

# ------------------------- Removing Items Using Del ------------------------- #
# The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely

# syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
# del lst        # to delete the list completely

# ---------------------------- Clearing List Items --------------------------- #
# The clear() method empties the list:

# syntax
# lst = ['item1', 'item2']
# lst.clear()

# ------------------------------ Copying a List ------------------------------ #
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a *reference* of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().

# syntax
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

# ------------------------------- Joining Lists ------------------------------ #
# There are several ways to join, or concatenate, two or more lists in Python.

# Plus Operator (+)

# syntax
# list3 = list1 + list2

# Joining using extend() method The extend() method allows to append list in a list. See the example below.

# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)

# ------------------------- Counting Items in a List ------------------------- #
# The count() method returns the number of times an item appears in a list:

# syntax
# lst = ['item1', 'item2']
# lst.count(item)

# ------------------------- Finding Index of an Item ------------------------- #
# The index() method returns the index of an item in the list:

# syntax
# lst = ['item1', 'item2']
# lst.index(item)

# ----------------------------- Reversing a List ----------------------------- #
# The reverse() method reverses the order of a list in place while [::-1] makes a copy

# syntax
# lst = ['item1', 'item2']
# lst.reverse()

# ---------------------------- Sorting List Items ---------------------------- #
# To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

# sort(): this method modifies the original list

# syntax
# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending

# sorted(): returns the ordered list without modifying the original list Example:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# # Reverse order
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits = sorted(fruits,reverse=True)
# print(fruits)     # ['orange', 'mango', 'lemon', 'banana']