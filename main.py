import operator
import re

# question 1
# name="chani"
# for item in name:
#     if item != 'a':
#         print (item,end=" ")
# print ()
# # question 2
# age = 12
# if age < 14:
#     print("kid")
# elif age < 20:
#     print("adult")
# # question 3
# x,y,z = "ester","cohen",18
# print ("the name is {} {} and the age is{}".format(x,y,z))
# # question 4 1
# sentence="welcome to our class"
# word=sentence.split(" ")
# print (word)
# # question 4 2
# word=["hello","class","nice"]
# sentence=" ".join(word)
# print (sentence)
# # exercise 2
# # question 1
# age = input ("enter your age")
# if age.isdigit():
#     print (int (age)*12)
# else:
#     print ("oops")
# # question 2
# list = []
# while True:
#     line =input("enter your sentences")
#     if line == "":
#         break
#     list.append(line)
# for line in reversed(list):
#     print(line)
# # question 3
# list=[]
# for i in range(2):
#    line= input("enter the rectangle")
#    if line.isdigit():
#        list.append(line)
#    else:
#        print("enter again")
# def func(list):
#     print ("the area is{}".format(int(list[0])*int(list[1])))
# func(list)
# # question 4
# list=[30,50,100,40]
# sum=0
# count=0
# for item in list:
#     sum+=item
#     count+=1
# print (sum/count)
# # question 5
# bool = 1
# line=int(input("enter a num"))
# for i in range(2,100):
#     if line %i==0:
#         print("not first")
#         bool = 0
#         break
#
# if bool ==1:
#     print ("first")
# # question 6
# rubi=60
# shimi=60
# sum=0
# if rubi >0 and shimi>0:
#     if sum%2==0:
#         rubi-=rubi/2
#         shimi+=rubi/2
#     else:
#         shimi -= shimi / 2
#         rubi += shimi / 2
#     sum+=1
#     if shimi==rubi:
#         print ("wow!they have the same")
# #strings
# # question 1
# str=input("enter a word")
# length=len(str)
# bool1=0
# for i,line in range(0,length):
#     if str[i]!=str[length]:
#         print("not palindrom")
#         bool1 =1
#         break
#     else:
#         length-=1
# if bool1==0:
#     print("pailndrom")
# # question 2
# sentence2=input("enter a sentence")
# list3=sentence2.split(" ")
# max=0
# for item in list3:
#     if len(item)>max:
#         max=len(item)
#         maxsentence=item
# print (maxsentence)
# # question 3
# word=input("enter a word")
# for item in word:
#     if item.islower():
#         print ("not all upper digits")
#
# חוברת תרגול
# תרגיל מספר 1
# ----touple--------
import random

l = [1, 2, 3, 4, 5, (1, 2, 3)]
count = 0
for item in l:
    if item == tuple:
        print("the count is:" + count)
    count = count + 1

# תרגיל מספר2
word = input("enter a word")
l = []
for item in word:
    l.append(item)
print(tuple(l))
# תרגיל מספר3
word2 = (1, 2, 3)
reserve = tuple(reversed(word2))
result = tuple(word2 + reserve)
print(result)


# ----------Dict-----------
# תרגיל מספר 1
def find_price(cars, model):
    if model in cars:
        return cars[model]
    else:
        return "this model is not exists"


# תרגיל מספר2
def Find_sugar(receipe):
    if "sugar" in receipe:
        print(receipe("sugar"))
    else:
        receipe.update({"sugar": 3})


# תרגיל מספר3
def reverse_dict(dict):
    reversed_dict = {}
    for key, value in dict.items():
        if value in reversed_dict:
            reversed_dict[value].append(key)
        else:
            reversed_dict[value] = key
    return reversed_dict


# ----------List-----------
# תרגיל מספר 1
def Reomve(list, value):
    new_list = []
    for num in list:
        if num != value:
            new_list.append(num)
    return new_list


# תרגיל מספר 2
list = []
for _ in range(5):
    new_scores = []
    for _ in range(10):
        new_scores.append((random.randint(0, 100)))
    list.append(new_scores)
print(list)
for listt in list:
    sum = 0
    count = 0
    for mark in listt:
        sum += mark
        count = count + 1
    print(sum / count)


# תרגיל מספר 3
def returnitems(list):
    return list[len(list) - 1] + list[len(list) - 2] + list[len(list) - 3]


# ---------Strings----------
# תרגיל מספר 1
def StringPalindrom():
    word = input("enter a string")
    len = word[-1]
    for i in word / 2:
        if word[i] != word[len]:
            print("not")
            break


print("Palindrom")
# -----rejex----------
#!!
# ----בדיקת כתובת-----
address = "pincas 7 bneibrak"


def Validateaddress(address):
    rejexaddress = '^[a-zA-Z]+/s[0-9]+/s[a-zA-Z]+$'
    if re.search(rejexaddress, address):
        return True
    return False


print(Validateaddress(address));
# ----בדיקת תז-----
tz = '326592656'


def ValidateTz(tz):
    rejexValidate = '[0-9]{9}'
    if re.search(rejexValidate, tz):
        return True
    return False


print(ValidateTz(tz));

#!!
# ----בדיקת פונקציה ב2 נעלמים x וy בלבד-----
def ValidateFunction(function):
    rejexfunction = "^[a-zA-Z0-9]{1,20}(x[a-zA-Z0-9]{1,20})?(y[a-zA-Z0-9]{1,20})?$"
    if re.search(rejexfunction, function):
        return True
    return False


function = "f(x)"
print(ValidateFunction(function))
#!!
# ---------אימות תאריך--------
Date = '06/06/2004'


def ValidateDate(date):
    regexdate = '[0-9]{2}\s[0-9]{2}\s[0-9]{4}'
    if re.search(regexdate, date):
        return True
    return False


print(ValidateDate(Date));
#-------פונקציות נוספות--------
#--------1---------
numbers={1,2,3,4,5}
numbers2={3,3,3,3,3}
numbers_to_check=3
result=numbers_to_check in numbers
result1=all(number==numbers_to_check for number in numbers2)
print(result)
print(result1)
print(numbers_to_check==max(numbers))
#--------2----------
string1=['yonatan']
string2=['blumental']
for string1,string2 in zip(string1,string2):
    print(f"שם: {string1}, שם משפחה: {string2}")
#------3---------
listother=[1,2,3,4,5,6]
for number in listother:
    if number ** 2 % 1 == 0:
        listother.remove(number)
for ir in listother:
    print(ir)
#-------4-----------
def multiply_by_two(numbers):
    for number in numbers:
        yield operator.lshift(number, 2)

numbers = [1, 2, 3, 4, 5, 6]

# מדפיסה את כל המספרים ברשימה כפול שניים
for number in multiply_by_two(numbers):
    print(number)
#----------5----------
students=["sari,avital,shoshi,nensi"]
print(f"name:{','.join(students)}")
#-----------6-------
code = """
def add(a, b):
    return a + b

print(add(1, 2))
"""

exec(code)

