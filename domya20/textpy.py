# myStr = "Python-cool!"
# print(myStr[1:3]) #yt
# print(myStr[-5:-2]) #coo
# print(myStr[-5:11]) #cool
# print(myStr[:6]) #Python
# print(myStr[6:]) #-cool!
# print(myStr[:-1]) #Python-cool
# print(myStr[:1])
# print(myStr[1:])
# print(myStr[-1:])
# print(myStr[-5:]) #cool
# print(myStr[5:])
import string

# myStr = "1234567890"
# print(myStr[2:8:2]) #357
# print(myStr[1:9:3])
# print(myStr[8:2:-2]) #975
# print(myStr[10:1:-3])
# print(myStr[::-1]) #0987654321
# print(myStr[5::2]) #680
# print(myStr[-1::-2]) #08642
# print(myStr[:len(myStr):4]) #159
# print(myStr[::4]) #159
#
# print("Python books:")
# print("\t'Python Programming: An Introduction to Computer Science'")
# print("\t'The Python Guide for Beginners'")
#
# yStr = "\x2C"
# print(myStr)
#
# print('\'\\Python Programming: An Introduction to Computer Science\'')
# print("\"Python Programming: An Introduction to Computer Science\"")
# print("15\\2")
#
# myStr = ("In Python strings, the backslash '\\' is a special character."
#        "It is used in representingcertain whitespace characters: '\\t' is a tab,'\\n' is a newline")
# print(myStr)
#
# normalText='''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n'''
# rawText=r'''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n
#  '''
# print(normalText)
# print(rawText)
#
# serLogin=input("Your login: ")
# print("Welcome,", serLogin, ". Let's start game!")
# strMsg="Dear, "+serLogin+". Game over!"
# print(strMsg)
#
# userLogin=input("Your login: ")
# strMsg="Welcome, {}. Let's start game!".format(userLogin)
# print(strMsg)

strMsg3 = ("My name is {name}, I'm {age}".
           format(name="Student",age=25))
print(strMsg3) # My name is Student, I'm 25
strMsg4 = ("My name is {name}, I'm {age}".
           format(age=25,name="Student"))
print(strMsg4) # My name is Student, I'm 25

strMsg = ("Your salary is {0:9.2f}".
          format(200.846))
print(strMsg) # Your salary is 200.8

# userNumber = int(input("Your number? ")) #255
# myStrB = ("The binary representation of a number {n}"
#           "is {n:b}".format(n=userNumber))
# print(myStrB) #The binary representation of a number255 is 11111111
#
# myStrO=("The octal representation of a number {n}"
#         "is {n:o}".format(n=userNumber))
# print(myStrO) #The octal representation of a number255 is 377
# myStrH=("The Hex representation of a number {n}"
#         "is {n:x}").format(n=userNumber)
# print(myStrH) #The Hex representation of a number 255 is ff

# myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
# print(myStr1) #The number1 range from -10 to 10
# myStr2="The number2 range from {0:+} to {1:+}".format(-20,50)
# print(myStr2) #The number2 range from -20 to +50
# myStr3="The number3 range from {0: } to {1:}".format(-30,30)
# print(myStr3) #The number3 range from -30 to 30

#установим доступное пространство для значения до 10 символов.
# myStr1 = "You have {:<10} points."
# print(myStr1.format(12)) #You have 12            points.
# myStr2 = "You have {:>10} points."
# print(myStr2.format(12)) #You have          12 points.
# myStr3 = "You have {:^10} points."
# print(myStr3.format(12)) #You have      12      points.

myStr1 = "Number is {:<10.2f}!"
print(myStr1.format(34.8256)) #Number is 34.83         !
myStr2 = "Number is {:>10.2f}!"
print(myStr2.format(34.8256)) #Number is           34.83!
myStr3 = "Number is {:^10.2f}!"
print(myStr3.format(34.8256)) #Number is    34.83     !

myStr1 = "Your login is {:<20}!"
print(myStr1.format("Admin")) #Your login is Admin                !
myStr2 = "Your password is {:>20}!"
print(myStr2.format("12345")) #Your password is               12345!
myStr3 = "Your secret word is {:^15}!"
print(myStr3.format("IT")) #Your secret word is       IT           !


import string as str

print(str.digits)

print("dfgdg\\\\")

zap =","
if zap in string.punctuation:
    print(zap)

import string
import random

userLogin = "".join(random.sample((string.ascii_lowercase), 6))
userPass = "".join(random.sample((string.ascii_letters +
                                         string.digits), 8))
print("login:", userLogin)
print("password:", userPass)

from string import Template
t = Template('$userName has the rights to $userRights in the $appName')
resStr = t.substitute(userName='Admin',
userRights = 'edit',
appName='SuperApp.')
print(resStr) #Admin has the rights to edit in the SuperApp

import re
userStr="abcd abc 123 efgh 456"
match = re.search(r'\d{3}', userStr)
print(match.group()) # 123

import re
userStr="30.11.2021 — 2021! Grand Prix Series, 14.12.2021 — Grand Pemio D'Italia; 27.12.2021 — Cup of Austria by IceChallenge!"
strList = re.split(r'[,;!]+', userStr)
print(strList[2]) #['30.11.2021 — 2021 Grand Prix Series',' 14.12.2021 — Grand Pemio D'Italia',' 27.12.2021 — Cup of Austria by IceChallenge']
courses =list(("Math", "Algorithms", "Databases"))
print(courses) #['Math', 'Algorithms', 'Databases']

sec_list =[2, 3, 1]
my_list =[4, "dfdg", 45, sec_list]
print(type(my_list))

import random
list1 = [random.randint(0, 101) for i in range(6)]

# list1 = [i*i for i in range(6)]

list2 = [i*2 for i in list1]
print(list2)
list3 = [i for i in list1 if i % 2 == 0]
print(list3)
# list[0]="First element"
print(list1.append("new"))

list1.insert(0, "newww le")
print(list1.index("newww le"))#['newww le', 2, 50, 34, 84, 29, 99, 'new']

print(list1)
print(list1[::2])


ne= "newww le"
print(ne in list1) #True



for i in list2:
    if i >10:
        print(i)


list2=[i+"*" for i in "example"]
print(list2) #['e*', 'x*', 'a*', 'm*', 'p*', 'l*', 'e*']

import random
list4=[random.randint(1, 200) for i in range(1,11) if i % 2 == 0]
# list4=[i*i for i in range(1,11) if i % 2 == 0]
print(list4)

list6 = [x*y for x in range(1, 4) for y in range(1, 4)]
print(list6) #[1, 2, 3, 2, 4, 6, 3, 6, 9]



# myCourses= ["Algorithms", 2345, 7009, "Networks", "Databases"]
# print(myCourses) #['Algorithms', 2345, 7009, 'Networks', 'Databases']
#
# customers=['Bob','Anna','Joe','Bob','Nick']
# list5= [i for i in customers if i!='Bob' and i!='Joe']
# print(list5) #['Anna', 'Nick']
#
#
#
# myCourses= ["Algorithms", 2345, 7009, "Networks", "Databases"]
# print(myCourses[1:3]) #[2345, 7009]
# print(myCourses[-4:-2]) #[2345, 7009]
# print(myCourses[1:-1]) #[2345, 7009, 'Networks']
# print(myCourses[:-1]) #['Algorithms', 2345, 7009, 'Networks']
# print(myCourses[3:]) #['Networks', 'Databases']
# print(myCourses[::2]) #['Algorithms', 7009, 'Databases']
# print(myCourses[::-1]) #['Databases', 'Networks', 7009, 2345, 'Algorithms']
# print(myCourses[-4::-1]) #[2345, 'Algorithms'
#
# category =["Drama", "Comedy", "Fantasy"]
# print(category) #['Drama', 'Comedy', 'Fantasy'
# category[-1]="Action"
# print(category) #['Drama', 'Comedy', 'Action']
#
#
# category=["Drama", "Comedy", "Mystery", "Romance", "Comedy"]
# category.sort()
# print(category) #['Comedy', 'Comedy', 'Drama', 'Mystery', 'Romance']
# category.sort(reverse=True)
# print(category) #['Romance', 'Mystery', 'Drama', 'Comedy', 'Comedy']
# prices=[100, 250.45, 1200, 20.78]
# prices.sort()
#
# customers=['Bob','Anna','Joe','Bob','Nick']
# print('Bob' in customers) #True
#
# ustomers=['Bob','Anna','Joe','Bob','Nick']
# if ('Bob' in customers):
#  print("Bob is our customer")
# else:
#  print("Sorry")

myTbl=[[111,112,113],[221,222,223]]
print(myTbl[1][1]) #222
print(myTbl[0]) #[111, 112, 113]

category =["Drama", "Comedy", "Mystery","Romance"]
for film in category:
 print(film)

#my_list = [1, 2, 3]
#print(my_list[2])
#
#my_en_list = [[1, 2], [3, 4], [5, 6]]
#
## print(my_en_list[-1][-2])
#
#for i in range(3):
#    for j in range(2):
#        print(f"index: [{i}][{j}] element:{my_en_list[i][j]}")

# import re
# userStr="30.11.2021 — 2021! Grand Prix Series, 14.12.2021 — Grand Pemio D'Italia; 27.12.2021 — Cup of Austria by IceChallenge!"
# strList = re.split(r'[,;!]+', userStr)
# print(strList[2]) #['30.11.2021 — 2021 Grand Prix Series',' 14.12.2021 — Grand Pemio D'Italia',' 27.12.2021 — Cup of Austria by IceChallenge']
# courses =list(("math", "Algorithms", "Databases"))
# print(courses) #['Math', 'Algorithms', 'Databases']