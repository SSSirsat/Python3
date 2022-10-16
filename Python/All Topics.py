Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
bycycles = ['herro', 'honda', 'motor', 'nitro', 'ranger']
print(bycycle[0])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(bycycle[0])
NameError: name 'bycycle' is not defined. Did you mean: 'bycycles'?
bycycles[0]
'herro'
bycycles[3]
'nitro'
message = f"My first bycycle name was a {bycycles[3].title()}"
print(message)
My first bycycle name was a Nitro
bycycles[0] = "ducati"
bycycles
['ducati', 'honda', 'motor', 'nitro', 'ranger']
bycycles.append("maruti")
bycycles
['ducati', 'honda', 'motor', 'nitro', 'ranger', 'maruti']
bycycles.insert(1,'atlas')
bycycles
['ducati', 'atlas', 'honda', 'motor', 'nitro', 'ranger', 'maruti']
len(bycycles)
7
del bycycles[2]
bycycles
['ducati', 'atlas', 'motor', 'nitro', 'ranger', 'maruti']
len(bycycles)
6
last_owned = bycycles.pop(0)
last_owned
'ducati'
bycycles
['atlas', 'motor', 'nitro', 'ranger', 'maruti']
len(bycycles)
5
bycycles.remove('maruti')
bycycles
['atlas', 'motor', 'nitro', 'ranger']
len(bycycles)
4
bycycles.sort()
bycycles
['atlas', 'motor', 'nitro', 'ranger']
bycycles[0] = 'xeros'
bycycles
['xeros', 'motor', 'nitro', 'ranger']
bycycles.append('car')
bycycles
['xeros', 'motor', 'nitro', 'ranger', 'car']
bycycles.sort()
bycycles
['car', 'motor', 'nitro', 'ranger', 'xeros']
sorted(bycycles)
['car', 'motor', 'nitro', 'ranger', 'xeros']
bycycles.reverse()
bycycles
['xeros', 'ranger', 'nitro', 'motor', 'car']
sorted(bycycles)
['car', 'motor', 'nitro', 'ranger', 'xeros']
reversed(bycycles)
<list_reverseiterator object at 0x00000297C14C5ED0>
bycycles
['xeros', 'ranger', 'nitro', 'motor', 'car']
len(bycycles)
5
for by in bycycles:
    print(by)

    
xeros
ranger
nitro
motor
car
for by in bycycles:
    return by.upper()
SyntaxError: 'return' outside function
for by in bycycles:
    print(by.upper())

    
XEROS
RANGER
NITRO
MOTOR
CAR
for by in bycycles:
    print(by.reverse())

    
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(by.reverse())
AttributeError: 'str' object has no attribute 'reverse'
for value in range(1,5):
    print(values)

    
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print(values)
NameError: name 'values' is not defined. Did you mean: 'value'?
for value in range(1,5)
SyntaxError: expected ':'
for value in range(1,5):
    print(value)

    
1
2
3
4
nunbers = list(range(1,6))
print(numbers)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(numbers)
NameError: name 'numbers' is not defined. Did you mean: 'nunbers'?
print(nunbers)
[1, 2, 3, 4, 5]
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)

    
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
min(squares)
1
max(squares)
100
sum(squares)
385
squares = [value**2 for value in range(1,11)]
squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
players = ['shuabhm', 'manish', 'shubha', 'chaitanys', 'seets','nisha']
players[0:3]
['shuabhm', 'manish', 'shubha']
players[3:5]
['chaitanys', 'seets']
 players[2:]
 
SyntaxError: unexpected indent
players[2:]
['shubha', 'chaitanys', 'seets', 'nisha']
players[-2:]
['seets', 'nisha']
for player in players[:4]:
    print(player.upper())

    
SHUABHM
MANISH
SHUBHA
CHAITANYS
players.append('shankarpadya')
players
['shuabhm', 'manish', 'shubha', 'chaitanys', 'seets', 'nisha', 'shankarpadya']
players.sort()
players
['chaitanys', 'manish', 'nisha', 'seets', 'shankarpadya', 'shuabhm', 'shubha']
dimension  = (100,200)
dir(dimension)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
dtype(dimension)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    dtype(dimension)
NameError: name 'dtype' is not defined. Did you mean: 'type'?
]
dimension.type()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dimension.type()
AttributeError: 'tuple' object has no attribute 'type'
dimension.dtype()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    dimension.dtype()
AttributeError: 'tuple' object has no attribute 'dtype'
type(dimension)
<class 'tuple'>
type(players)
<class 'list'>
my_t = (3,)
my_t
(3,)
car = 'audi'
car == 'bmw'
False
car.lower()
'audi'
car = "Audi"
car.lower() == 'audi'
True
age = 18
age == 18
True
age > 1 7
SyntaxError: invalid syntax. Perhaps you forgot a comma?
age > 17
True
age< 17
False
age <17 and age > 19
False
id(age)
2850769470224
if age >=18:
    print("You are old enough ot vote")

    
You are old enough ot vote
if age >=18:
    print("You are old enough ot vote")
    print("are you registeres for voating")

    
You are old enough ot vote
are you registeres for voating
if age < 4"
SyntaxError: unterminated string literal (detected at line 1)
if age < 4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20

    
print(f"Yur admission  cost is Rs.{price}.")
Yur admission  cost is Rs.40.
#Dictioneries
alien = {'color':'green', 'point':5}
alien
{'color': 'green', 'point': 5}
alien['color']
'green'
alien['point']
5
new_points = alien['point']
print(f"You just earned {new_points} points!!")
You just earned 5 points!!
alien['x_pos'] = 0
alien['y_pos'] = 34
alien
{'color': 'green', 'point': 5, 'x_pos': 0, 'y_pos': 34}
if alien['x_pos'] == slow:
    x_increament =1
elif alien['x_pos'] == 0:
    x_increament = 2

    
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    if alien['x_pos'] == slow:
NameError: name 'slow' is not defined
if alien['x_pos'] == slow:
    x_increament =1
elif alien['x_pos'] == 0:
    x_increament = 2
else:
    x_increament = 3

    
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    if alien['x_pos'] == slow:
NameError: name 'slow' is not defined
language = alien['color'].title()
language
'Green'
fav_lan = {
    'jen' : 'C++',
    'shubham':'Python',
    'sarah':'ruby',
    'pahil':'pyhton',
    'manish':'Java'
    }
for name,language in fav_lan.items():
    print(f"Student Name:{name.title()} and favorite langusge is:{language.title()}.")

    
Student Name:Jen and favorite langusge is:C++.
Student Name:Shubham and favorite langusge is:Python.
Student Name:Sarah and favorite langusge is:Ruby.
Student Name:Pahil and favorite langusge is:Pyhton.
Student Name:Manish and favorite langusge is:Java.
for name,language in fav_lan.items():
    print(f"Student Name:{name.upper()} and favorite langusge is:{language.lower()}.")

    
Student Name:JEN and favorite langusge is:c++.
Student Name:SHUBHAM and favorite langusge is:python.
Student Name:SARAH and favorite langusge is:ruby.
Student Name:PAHIL and favorite langusge is:pyhton.
Student Name:MANISH and favorite langusge is:java.


len(fav_lan)
5
name = input("Please Enter Your Name:")
Please Enter Your Name:shuabm sirsat
print(f"hello, {name}.)
      
SyntaxError: unterminated string literal (detected at line 1)
print(f"hello, {name}")
      
hello, shuabm sirsat
cur_num = 1
      
while cur_num <=10:
    print(cur_num)
    cur_num +=1

    
1
2
3
4
5
6
7
8
9
10
def greet_fun():
    print("Hello")

    
greet_fun()
Hello
def uername(name):
    print(f"Hello,{name}.upper()")

    
uername('shubham')
Hello,shubham.upper()
def uername(name):
    print(f"Hello,{name.upper()}")

    
uername("masnish")
Hello,MASNISH
