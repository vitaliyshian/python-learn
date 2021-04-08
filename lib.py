# print('<a href="http://google.com"></a>')
'''
x = 1
if x == 1:
    print("x is 1")
else:
    print("x is not 1")
'''

# типы данных числа
'''
1 целое
7 целое
3.5 вещественное
0 целое
0.0 целое
1.2 вещественное
0.0001 вещественное
777 целое
100.000 целое
77.77 вещественное
123 целое
357.00 целое
13 целое
0.000000 целое
'''
# интеджер
# типы данных
'''
int - целое число 778
float - вещественное число 17.494590
string - строка "hello" 
isinstance - проверка на тип данных
'''
'''
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

myint = int(7.57577)
print(myint)

mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

mystring = 'Don\'t worry about apostrophes'
print(mystring)
'''
'''
one = 1
two = 2
three = one + two
print(three)

sum = one / two
print(sum)

sum = one * two
print(sum)

sum = one - two
print(sum)
'''
'''
hello = 'hello'
world = 'world'
helloworld = hello + ' ' + world # конкатенация строк
print(helloworld)

x = 'x'
y = 'y'
z = 'z'
print(x + ' + ' + y + ' + ' + z + ' = 0')

x = 'x'
y = 'y'
z = 'z'
print(x + ' ' + '+' + ' ' + y + ' ' + '+' + ' ' + z + ' = 0')

x = 'a'
y = 'b'
z = 'c'
print(x + ' ' + '+' + ' ' + y + ' ' + '+' + ' ' + z + ' = 0')
'''
'''
a, b, c = 3, 4, 5 # синтаксический сахар
print(a,b,c)
'''
'''
one = 1
two = 2
hello = 'hello'
print(str(one) + str(two) + hello)
'''
'''
mystring = 'hello'
myfloat = 10.0
myint = 20

if (mystring == 'hello'):
    print("String: %s" % mystring)

if (isinstance(myfloat,float) and myfloat == 10.0):# проверка переменных на тип данных
    print("Float: %f" % myfloat)

if (isinstance(myint, int) and myint == 20):
    print("Integer: %d" % myint)

print("String:" + mystring + ', ' + "Float:" + str(myfloat) + ", " + "Integer:" + str(myint))# конкатенация строк
print("String: %s, Float: %f, Integer: %d" % (mystring, myfloat, myint))# форматирование строк
'''
'''
x = "hello"

if isinstance(x, str):
    print("x is string")
'''
'''
number1 = 20
number2 = 30
sum1 = number2 * number1
print("Задание 1 " + "Результат:" + str(sum1))

number3 = 40
number4 = 30
sum2 = number3 + number4
print("Задание 2 " + "Результат:" + str(sum2))
'''
'''
spells = [
    "Riddikulus!",
    "Wingardium Leviosa",
    "Avada Kedavra",
    "Expecto Patronum",
    "Nox",
    "Lumos"
    ]
print(spells[3])
'''
'''
mylist = [4, 5, 6]
mychars = ["c", "d", "a", "b"]
mylist.append(1) # добавление елементов в лист
mylist.append(2)
mylist.append(3)
# print(mylist)

mylist.sort()
mychars.sort()

sum = mylist + mychars

 print(mylist)
# print(sum[1], sum[3], sum[5])

# [4, 5, 6, 'a', 'b', 'c', 1, 2, 3]
# [1, 2, 3, 4, 5, 6, a, b, c]
'''
'''
mylist = [1, 2, 3, 4, 5, 6]

mylist[0] = mylist[0] * 2
mylist[1] = mylist[1] * 2
mylist[2] = mylist[2] * 2
mylist[3] = mylist[3] * 2
mylist[4] = mylist[4] * 2
mylist[5] = mylist[5] * 2

'''
'''
mylist = [1, 2, 3, 4, 5, 6]
i = 0
for val in mylist:
    mylist[i] = val * 2
    i = i + 1

print(mylist)
'''

'''
for i in range(10):
    print("Итерация Номер: %d Завершена" % i)
# print("String: %s, Float: %f, Integer: %d" % (mystring, myfloat, myint))
'''

'''
существует массив чисел
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

1. посчитать сумму всех чисел
2. умножить все числа друг на друга, например: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8
'''
'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
sum = mylist[0] * mylist[1] * mylist[2] * mylist[3] * mylist[4] * mylist[5] * mylist[6] * mylist[7]

print(sum)
'''
'''
mylist = [2, 9, 1, 4, 1, 7, 7, 7, 10, 6, 3, 1, 7, 0, 6, 6, 9, 0, 7, 4, 3, 9, 1, 5, 0, 0, 0, 10, 8, 0, 6, 10, 3, 6, 0, 8, 3, 7, 7, 8, 3, 5, 3, 10, 3, 7, 4, 0, 6, 8, 10, 1, 2, 10, 4, 1, 5, 8, 6, 8, 10, 3, 4, 4, 9, 7, 8, 6, 9, 0, 7, 3, 6, 6, 10, 2, 5, 8, 10, 5, 1, 7, 10, 8, 1, 2, 8, 6, 5, 7, 0, 7, 0, 4, 9, 9, 9, 6, 10, 2, 2, 8, 3, 0, 3, 8, 8, 3, 6, 8, 5, 9, 5, 7, 4, 10, 8, 9, 0, 6, 8, 2, 8, 8, 3, 6, 0, 7, 5, 9, 8, 3, 8, 6, 7, 5, 6, 5, 0, 8, 8, 9, 9, 5, 7, 9, 0, 3, 10, 2, 8, 9, 2, 1, 8, 4, 0, 10, 1, 1, 0, 7, 0, 4, 3, 4, 1, 9, 2, 5, 4, 1, 2, 2, 4, 8, 2, 10, 4, 10, 4, 7, 5, 7, 7, 1, 0, 4, 6, 5, 6, 3, 4, 1, 4, 8, 3, 9, 6, 0, 3, 0, 6, 2, 0, 2, 7, 8, 10, 6, 8, 3, 10, 8, 7, 3, 8, 10, 0, 6, 10, 9, 5, 10, 10, 6, 0, 4, 2, 3, 0, 4, 1, 1, 4, 4, 2, 6, 9, 4, 2, 0, 8, 0, 9, 3, 9, 7, 2, 9, 8, 0, 6, 3, 5, 1, 3, 9, 10, 6, 9, 3, 7, 1, 10, 6, 4, 8, 7, 0, 5, 9, 6, 4, 0, 2, 3, 5, 9, 2, 5, 6, 3, 4, 10, 1, 6, 8, 5, 10, 8, 7, 8, 3, 1, 0, 1, 2, 2, 2, 8, 3, 4, 5, 9, 8, 4, 5, 5, 5, 1, 4, 3, 9, 7, 2, 9, 8, 1, 5, 0, 6, 1, 6, 2, 2, 5, 1, 9, 9, 6, 1, 9, 8, 3, 9, 1, 4, 5, 4, 9, 8, 1, 7, 4, 1, 0, 4, 0, 9, 10, 0, 1, 6, 1, 0, 3, 3, 9, 6, 2, 1, 7, 2, 10, 3, 2, 1, 6, 6, 8, 4, 8, 4, 7, 5, 1, 3, 10, 5, 0, 0, 0, 4, 9, 5, 7, 6, 5, 6, 1, 1, 5, 9, 7, 1, 4, 3, 9, 8, 7, 10, 5, 4, 2, 8, 3, 4, 3, 3, 5, 1, 4, 1, 7, 1, 10, 9, 10, 5, 3, 6, 4, 0, 5, 2, 5, 9, 4, 3, 5, 1, 8, 9, 9, 9, 1, 3, 3, 0, 3, 6, 1, 4, 8, 1, 1, 0, 10, 0, 4, 5, 7, 7, 2, 1, 8, 5, 1, 8, 10, 2, 2, 2, 2, 5, 4, 1, 8, 9, 4, 2, 3, 2, 8, 0, 5, 9, 10, 8, 3, 2, 4, 6, 8, 2, 0, 10, 3, 4, 1, 10, 7, 6, 8, 4, 8, 7, 8, 7, 0, 6, 5, 2, 4, 7, 0, 10, 6, 9, 0, 0, 5, 9, 2, 9, 2, 2, 4, 4, 6, 9, 6, 2, 9, 1, 3, 7, 0, 2, 8, 5, 8, 10, 7, 10, 10, 3, 3, 5, 7, 10, 7, 3, 6, 5, 8, 9, 10, 4, 10, 3, 0, 1, 8, 10, 5, 2, 8, 3, 4, 4, 4, 8, 5, 2, 7, 9, 1, 1, 9, 8, 9, 6, 2, 2, 4, 6, 3, 9, 0, 7, 10, 6, 10, 5, 6, 8, 2, 8, 0, 8, 1, 4, 10, 1, 4, 1, 2, 9, 10, 10, 1, 7, 3, 6, 6, 6, 2, 5, 7, 2, 9, 7, 3, 1, 6, 9, 8, 6, 1, 10, 4, 4, 3, 6, 8, 0, 3, 8, 7, 9, 0, 0, 10, 9, 3, 4, 3, 2, 4, 2, 8, 3, 4, 4, 9, 4, 10, 7, 2, 8, 5, 7, 6, 1, 3, 9, 6, 3, 4, 1, 0, 1, 9, 0, 8, 4, 10, 10, 2, 1, 8, 5, 9, 4, 6, 8, 10, 5, 8, 5, 0, 1, 7, 7, 5, 4, 8, 6, 5, 10, 9, 7, 1, 10, 6, 6, 3, 8, 0, 4, 10, 9, 8, 3, 7, 9, 8, 6, 4, 2, 7, 9, 10, 8, 3, 5, 8, 0, 10, 6, 9, 6, 6, 5, 9, 9, 1, 7, 3, 10, 10, 4, 10, 0, 6, 10, 2, 10, 6, 4, 2, 1, 9, 0, 5, 4, 6, 10, 8, 4, 2, 7, 4, 7, 2, 7, 8, 0, 4, 8, 1, 9, 6, 1, 5, 1, 10, 7, 0, 2, 8, 2, 1, 6, 10, 4, 9, 4, 3, 8, 3, 3, 5, 4, 1, 1, 8, 10, 5, 7, 8, 8, 0, 2, 4, 10, 8, 4, 5, 9, 3, 6, 8, 6, 2, 7, 4, 9, 5, 3, 4, 9, 3, 10, 0, 9, 6, 5, 6, 3, 4, 3, 1, 10, 2, 9, 7, 9, 2, 9, 4, 7, 8, 2, 2, 2, 7, 5, 4, 6, 3, 1, 3, 10, 4, 1, 1, 3, 6, 5, 7, 1, 2, 0, 0, 9, 0, 3, 10, 0, 7, 8, 9, 7, 5, 10, 4, 1, 9, 2, 1, 3, 6, 3, 7, 7, 6, 2, 3, 3, 4, 7, 8, 9, 6, 3, 7, 4, 5, 7, 9, 1, 3, 1, 0, 0, 0, 7, 5, 6, 9, 4, 3, 6, 2, 10, 2, 0, 0, 6, 2, 10, 8, 0, 9, 6, 4, 2, 1, 7, 10, 4, 0, 0, 8, 0, 8, 2, 0, 4, 1, 6, 1, 3, 0, 7, 10, 2, 4, 10, 3, 10, 7, 6, 5, 10, 4, 4, 10, 10, 3, 3, 0, 9, 9, 2, 5, 6, 9, 8, 10, 8, 0, 5, 8, 6, 8, 3, 8, 6, 10, 1, 4, 9, 1, 4, 2, 1, 2, 0, 3, 6, 0, 0, 10, 1, 8, 7, 8, 5, 1, 5, 0, 2, 8, 0, 7, 10]
sum = 0
count = 0

for val in mylist:
    sum = sum + val # сумма всех чисел в листе
    count = count + 1 # количество елементов в листе

print(sum, count)
'''
'''
mylist = [2, 9, 1, 4, 1, 7, 7, 7, 10, 6, 3, 1, 7, 0, 6, 6, 9, 0, 7, 4, 3, 9, 1, 5, 0, 0, 0, 10, 8, 0, 6, 10, 3, 6, 0, 8, 3, 7, 7, 8, 3, 5, 3, 10, 3, 7, 4, 0, 6, 8, 10, 1, 2, 10, 4, 1, 5, 8, 6, 8, 10, 3, 4, 4, 9, 7, 8, 6, 9, 0, 7, 3, 6, 6, 10, 2, 5, 8, 10, 5, 1, 7, 10, 8, 1, 2, 8, 6, 5, 7, 0, 7, 0, 4, 9, 9, 9, 6, 10, 2, 2, 8, 3, 0, 3, 8, 8, 3, 6, 8, 5, 9, 5, 7, 4, 10, 8, 9, 0, 6, 8, 2, 8, 8, 3, 6, 0, 7, 5, 9, 8, 3, 8, 6, 7, 5, 6, 5, 0, 8, 8, 9, 9, 5, 7, 9, 0, 3, 10, 2, 8, 9, 2, 1, 8, 4, 0, 10, 1, 1, 0, 7, 0, 4, 3, 4, 1, 9, 2, 5, 4, 1, 2, 2, 4, 8, 2, 10, 4, 10, 4, 7, 5, 7, 7, 1, 0, 4, 6, 5, 6, 3, 4, 1, 4, 8, 3, 9, 6, 0, 3, 0, 6, 2, 0, 2, 7, 8, 10, 6, 8, 3, 10, 8, 7, 3, 8, 10, 0, 6, 10, 9, 5, 10, 10, 6, 0, 4, 2, 3, 0, 4, 1, 1, 4, 4, 2, 6, 9, 4, 2, 0, 8, 0, 9, 3, 9, 7, 2, 9, 8, 0, 6, 3, 5, 1, 3, 9, 10, 6, 9, 3, 7, 1, 10, 6, 4, 8, 7, 0, 5, 9, 6, 4, 0, 2, 3, 5, 9, 2, 5, 6, 3, 4, 10, 1, 6, 8, 5, 10, 8, 7, 8, 3, 1, 0, 1, 2, 2, 2, 8, 3, 4, 5, 9, 8, 4, 5, 5, 5, 1, 4, 3, 9, 7, 2, 9, 8, 1, 5, 0, 6, 1, 6, 2, 2, 5, 1, 9, 9, 6, 1, 9, 8, 3, 9, 1, 4, 5, 4, 9, 8, 1, 7, 4, 1, 0, 4, 0, 9, 10, 0, 1, 6, 1, 0, 3, 3, 9, 6, 2, 1, 7, 2, 10, 3, 2, 1, 6, 6, 8, 4, 8, 4, 7, 5, 1, 3, 10, 5, 0, 0, 0, 4, 9, 5, 7, 6, 5, 6, 1, 1, 5, 9, 7, 1, 4, 3, 9, 8, 7, 10, 5, 4, 2, 8, 3, 4, 3, 3, 5, 1, 4, 1, 7, 1, 10, 9, 10, 5, 3, 6, 4, 0, 5, 2, 5, 9, 4, 3, 5, 1, 8, 9, 9, 9, 1, 3, 3, 0, 3, 6, 1, 4, 8, 1, 1, 0, 10, 0, 4, 5, 7, 7, 2, 1, 8, 5, 1, 8, 10, 2, 2, 2, 2, 5, 4, 1, 8, 9, 4, 2, 3, 2, 8, 0, 5, 9, 10, 8, 3, 2, 4, 6, 8, 2, 0, 10, 3, 4, 1, 10, 7, 6, 8, 4, 8, 7, 8, 7, 0, 6, 5, 2, 4, 7, 0, 10, 6, 9, 0, 0, 5, 9, 2, 9, 2, 2, 4, 4, 6, 9, 6, 2, 9, 1, 3, 7, 0, 2, 8, 5, 8, 10, 7, 10, 10, 3, 3, 5, 7, 10, 7, 3, 6, 5, 8, 9, 10, 4, 10, 3, 0, 1, 8, 10, 5, 2, 8, 3, 4, 4, 4, 8, 5, 2, 7, 9, 1, 1, 9, 8, 9, 6, 2, 2, 4, 6, 3, 9, 0, 7, 10, 6, 10, 5, 6, 8, 2, 8, 0, 8, 1, 4, 10, 1, 4, 1, 2, 9, 10, 10, 1, 7, 3, 6, 6, 6, 2, 5, 7, 2, 9, 7, 3, 1, 6, 9, 8, 6, 1, 10, 4, 4, 3, 6, 8, 0, 3, 8, 7, 9, 0, 0, 10, 9, 3, 4, 3, 2, 4, 2, 8, 3, 4, 4, 9, 4, 10, 7, 2, 8, 5, 7, 6, 1, 3, 9, 6, 3, 4, 1, 0, 1, 9, 0, 8, 4, 10, 10, 2, 1, 8, 5, 9, 4, 6, 8, 10, 5, 8, 5, 0, 1, 7, 7, 5, 4, 8, 6, 5, 10, 9, 7, 1, 10, 6, 6, 3, 8, 0, 4, 10, 9, 8, 3, 7, 9, 8, 6, 4, 2, 7, 9, 10, 8, 3, 5, 8, 0, 10, 6, 9, 6, 6, 5, 9, 9, 1, 7, 3, 10, 10, 4, 10, 0, 6, 10, 2, 10, 6, 4, 2, 1, 9, 0, 5, 4, 6, 10, 8, 4, 2, 7, 4, 7, 2, 7, 8, 0, 4, 8, 1, 9, 6, 1, 5, 1, 10, 7, 0, 2, 8, 2, 1, 6, 10, 4, 9, 4, 3, 8, 3, 3, 5, 4, 1, 1, 8, 10, 5, 7, 8, 8, 0, 2, 4, 10, 8, 4, 5, 9, 3, 6, 8, 6, 2, 7, 4, 9, 5, 3, 4, 9, 3, 10, 0, 9, 6, 5, 6, 3, 4, 3, 1, 10, 2, 9, 7, 9, 2, 9, 4, 7, 8, 2, 2, 2, 7, 5, 4, 6, 3, 1, 3, 10, 4, 1, 1, 3, 6, 5, 7, 1, 2, 0, 0, 9, 0, 3, 10, 0, 7, 8, 9, 7, 5, 10, 4, 1, 9, 2, 1, 3, 6, 3, 7, 7, 6, 2, 3, 3, 4, 7, 8, 9, 6, 3, 7, 4, 5, 7, 9, 1, 3, 1, 0, 0, 0, 7, 5, 6, 9, 4, 3, 6, 2, 10, 2, 0, 0, 6, 2, 10, 8, 0, 9, 6, 4, 2, 1, 7, 10, 4, 0, 0, 8, 0, 8, 2, 0, 4, 1, 6, 1, 3, 0, 7, 10, 2, 4, 10, 3, 10, 7, 6, 5, 10, 4, 4, 10, 10, 3, 3, 0, 9, 9, 2, 5, 6, 9, 8, 10, 8, 0, 5, 8, 6, 8, 3, 8, 6, 10, 1, 4, 9, 1, 4, 2, 1, 2, 0, 3, 6, 0, 0, 10, 1, 8, 7, 8, 5, 1, 5, 0, 2, 8, 0, 7, 10]
count = 0

for val in mylist:
    # 2 : 1
    # 9 : 2
    # 6 : 10
    # x : 737
    count = count + 1
    if count == 737:
        print(val)

print(mylist[736])
'''
'''
number = 1 + 2 * 3 / 4 # (1+2)умножение деление сложение
remainder = 12 % 3 # остаток от деления
squared = 2 ** 64 # возведение в степень


mylist = []
for i in range(5):
    mylist.append("h")
    mylist.append("e")
    mylist.append("l")
    mylist.append("l")
    mylist.append("o")
    print(mylist)
'''
'''
x = [2, 4, 6, 8]
y = [1, 3, 5, 7]
sum = x + y

sum.sort(reverse=True)

print(sum)
'''
'''
mylist = [8, 12, 34, 1, 0, 8, 6, 7, 23, 7, 5, 11, 29, 67, 144, 3, 2, 90]

'''
'''
mylist = [2, 3, 5, 6, "b", "c", "d", 7, "a", "g"]
text = []
int = []

for val in mylist:
    if isinstance(val, str):
        text.append(val)
    else:
        int.append(val)

text.sort(reverse=True)
int.sort(reverse=True)
print(text, int)
'''
'''
y = 1900

for x in range(121):
    y = y + 1
    print("Current year is %d " % y)
'''
'''
mylist = [1, 2, 3]
sum = mylist * 3 # скопировать масив 3 раза

print(sum)
'''
'''
name = "John"
age = 34
str = "My name is %s. My age is %d. It's my info" % (name, age)

print(str)
'''
'''
mylist = [1, 2, 3] # масив может быть выведен как строка
print("A list: %s" % mylist)
'''
'''
z = 10
print("Precision: %X" % z)
# 0 1 2 3 4 5 6 7 8 9 - десятиричная система исчисления DEC
# 0 1 2 3 4 5 6 7 8 9 A B C D E F - 16 ричная система исчисления HEX
# 0 1 2 3 4 5 6 7 8 - 8 ричная система исчисления OCT
# 0 1 - 2 ичная система исчисления BIN
'''
'''
2, 144, 16, 32, 3, 7, 8, 5, 14

представить и вывести эти числа в виде

2ичных
8миричных
16тиричных
'''
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
# 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10
# 1000


# bin = [10, 10010000, 10000, 100000, 11, 111, 1000, 101, 1110]
# oct = [2, 220, 20, 40, 3, 7, 10, 5, 16]
# hex = [2, 90, 10, 20, 3, 7, 8, 5, "E"]
'''
numbers = [2, 144, 16, 32, 3, 7, 8, 5, 14]

for val in numbers:
    bin2 = bin(val)
    oct8 = oct(val)
    hex16 = hex(val)
    print("Binary (BIN, Двоичный): %s\nOctal (OCT, Восьмиричный): %s\nHexadecimal (HEX, шеснадцатиричный) %s\n" % (bin2, oct8, hex16))
'''
'''
hello = "Hello World!"
hello2 = 'Hello World!'

x = len(hello) # Получить длину строки
y = len(hello2) # Получить длину строки
print(x, y)
'''
'''
hello = "Hello World!"
idx = hello.index("o")
idx2 = hello.index("!")
idx3 = None
try:  # В случае ошибки переведет выполнение в except
    idx3 = hello.index("z")
except:
    print("Error")
print(idx, idx2, idx3)
'''
'''
hello = "Hello World!"
x = hello.count("Hello") # Посчитать количество букв (L) в строке
print(x)
'''
'''
hello = 'This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end".'
#print(hello[0:128])# Выбать подстроку из строки

hello2 = "Hello World!"
print(hello2[0:5])
print(hello2[0:5:4])
print(hello2[::-1]) # Выборка с конца
'''
'''
hello = "hello world!"
caps = "HELLO WORLD!"
x = hello.upper() # Делает все большие буквы
y = caps.lower() # Делает все маленькие буквы
print(y)
'''
'''
hello = "Hello World!"
x = hello.startswith("Hello") # Проверяет начинается ли строка с определенной подстроке
y = hello.endswith("xdfhhhh!") # Проверяет заканчивается ли строка с определенной подстроке
print(x,y)
'''
'''
hello = "Hello World! Hello People!"
fruits = "Apple,Banana,Melon,Watermelon"
chunks = hello.split(" ") # Разделяем строку на состовляющие с помощью символа сепоратора после чего получаем масив из составных частей строки
chunks2 = fruits.split(",")
print(chunks, chunks2)
'''

'''
names = ["john", "ivan", "vitaliy", "alex", "arina", "garik"]

for val in names:
    names2 = val.capitalize()
    print("Муня зовут %s" % names2)
'''

'''
names = ["john", "ivan", "vitaliy", "alex", "arina", "garik"]
age = [65, 56, 26, 27, 25, 89]
c = 0
for val in names:
    name = val.capitalize()
    print("Муня зовут %s.Мне %d. Лет" % (name, age[c]))
    c = c + 1
'''
'''
names = ["john", "ivan", "vitaliy", "alex", "arina", "garik"]
cnames = []

for val in names:
    name = val.capitalize()
    cnames.append(name)

print(cnames)
'''
'''
x = 2
print(x == 2) # Логическое сравнение
print(x == 3) # Логическое сравнение
print(x < 3) # Логическое сравнение
'''
'''
name = "Rick"
age = 23

if name == "John" and age == 23:
    print("Your name is John and your age is 23")

if name == "John" or name == "Rick":
    print("Your name is John or Rick")
'''
'''
names = ["John", "Ivan", "Vitaliy", "Alex", "Arina", "Garik", "Rick"]
name = "Rick"

if name in names:
    print("Your name is %s" % name)

if name in ["John", "Ivan", "Vitaliy", "Alex", "Arina", "Garik", "Rick"]:
    print("Your name is %s" % name)
'''
# or - или
# True or True = True
# True or False = True
# False or False = False
# =========================
# and - и
# True and True = True
# True and False = False
# False and False = False
# ===========================
'''
x = 2
print(x != 2)# False
print(x != 3)#True
print(x >= 2)#True
print(x <= 2)#True
'''
'''
name = "Alex"

if name == "John":
    print("1")
elif name == "Rick":
    print("2")
elif name == "Alex":
    print("3")
elif name == "Andrey":
    print("4")
else:
    print("5")
'''
'''
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
'''
'''
x = [1, 2, 3]
y = x 
print(x is y)
'''
# изменить значения переменных так, что бы все условия отрабатывали с True

'''
number = 16
second_number = 0
first_array = [1, 1, 0]
second_array = [1, 2]

# Не МЕнять условие

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
'''

'''
primes = [1, 2, 3, 4]

for val in primes:
    print("For 1 - %d" % val)

for i in range(5):
    print("For 2 - %d"% i)

for i in range(3, 6):
    print("For 3 - %d" % i)

for i in range(1, 10, 2):
    print("For 4 - %d" % i)
'''
'''
count = 0

while count < 5:
    print(count)

    count = count + 1
'''
'''
import time
switch = True
timeout = time.time() + 5

while switch:
    print("Действие совершино! %s " % switch)
    if time.time() > timeout:
        switch = False

'''
'''
while True:
    print("Бесконечный цикл")
'''
'''
primes = [5, 6, 7, 8, 9, 10]
count = 0

while count < 6:
    print(primes[count])
    count = count + 1
'''

'''
count = 0

while True:
    print(count)
    count = count + 1
    if count >= 122:
        break #  Завершение цикла
'''
'''
for val in range(10): 
    if val % 2 != 0: # Проверка на четность !!!
        continue # Пропуск текущей итерации
    print(val)
'''
'''
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print("Count is %s" % count)
'''
'''
for val in range(1, 10):
    if val % 5 == 0:
        break
    print(val)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
'''

#1. все четные элементы сложить в массив even = []

#2. все нечетные элементы сложить в массив odd = []
'''
even = []
odd = []
numbers = [2,
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for val in numbers:
    if val % 2 == 0:
        even.append(val)
    else:
        odd.append(val)

print("Не четные цифры %s" % odd)
print("Четные цифры %s" % even)


mylist = [1, 2, 3, 4, 5, 6, 7, 8]
mylist2 = sum(mylist)

print("Сумма  Сложения всех чисел в масиве %s" % mylist2)
'''
'''
count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    if is_even(count[i]):
        print("%s Четное" % count[i])
    else:
        print("%s Не четное" % count[i])
'''

'''
1. Изменить функцию с именем list_benefits(), которая должна возвращать следующий список (массив) строк: 
	"Более организованный код", 
	"Более читаемый код", 
	"Упрощенное повторное использование кода",
	"Разрешить программистам совместно использовать код"

2. Изменить функцию с именем build_sentence(info), 
которая получает единственный аргумент benefit, содержащий строку, 
и возвращает предложение, начинающееся с данной строки
и заканчивающееся строкой "- это преимущество функций!"

Пример работы:
Более организованный код - это преимущество функций!
Более читаемый код - это преимущество функций!
Упрощенное повторное использование кода - это преимущество функций!
Разрешить программистам совместно использовать код - это преимущество функций!
'''

'''
def list_benefits():
   x = [
        "Более организованный код",
        "Более читаемый код",
        "Упрощенное повторное использование кода",
        "Разрешить программистам совместно использовать код"
     ]
   return x

def build_sentence(benefit):
    return "%s - это преимущество функций!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
'''
'''
raw = [1, 2, 3, 3, 3, 3, 4, 5] # Выборка уникальных елементов из масива
unique = []

for val in raw:
    if val not in unique:
        unique.append(val)

print(unique)
'''
'''
a = [2, 44, 444, 4, 4, 4, 4, 2]
b = [7, 7, 7, 7, 7, 6]
c = [1, 2, 3, 4, 4, 5, 5, 6, 7, 0]
d = [8, 8, 9, 0, 0, 5, 5, 8, 8, 0]
e = [3, 3, 3, 3, 3]
f = [0]
g = [1, 1, 0, 0]
q = []



def unique(raw, sort = False):
    un = []
    for val in raw:
        if val not in un:
            un.append(val)
    un.sort(reverse=sort)
    return un
'''