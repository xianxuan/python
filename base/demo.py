#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print()
print('\\\t\\')
print(r'\\\t\\')  # r''表示''内部的字符串默认不转义
print('''line1
line2
line3''')  # 多行表示
print(r'''hello,\n
world''')

# 基本类型
# 空值是Python里一个特殊的值，用None表示
a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)
# 全部大写的变量名表示常量当然如果你硬要是改变也没人能拦住你
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
# 整数没有大小限制；浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
print(ord('A'))
print(chr(65))
# bytes类型的数据用带b前缀的单引号或双引号表示
b = b'ABC'
print(b)

# 编码
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

# print（）和format
print('Hi, %s, you have $%d.' % ('Michael', 1000000))  # %f浮点数%x十六进制数
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%3d-%02d' % (3, 1))
print('%.3f' % 3.1415926)
# %s永远起作用，它会把任何数据类型转换为字符串
# 用%%来表示一个%
print("%d%%" % 7)
print('Hello, {}, 成绩提升了 {:.2f}'.format('小明', 17.125))

# list
# list有序集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
# pop删除
print(classmates.pop())
print(classmates.pop(1))
classmates[1] = 'Sarah'
print(classmates)
# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])

# tuple
# 有序列表叫元组tuple一旦初始化就不能修改(tuple的每个元素，指向永远不变)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
# 可变的tuple
t = ('a', 'b', ['A', 'B'])
print(t)
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
x = 1
if x:  # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
    print('True')

# birth = input('birth: ')#获得用户输入返回字符串
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# range()函数，可以生成一个整数序列
print(list(range(5)))
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# dict
# dict字典（Map）
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
d['Adam'] = 67
print(d)
print(d['Bob'])
# 通过in判断key是否存在
print('Thomas' in d)
# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
# dict中的key必须是不可变的不能是list

# set
# 要创建一个set，需要提供一个list作为输入集合
# 一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 可变对象和不可变对象
# list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)
# string是不可变对象
a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)
# abs(求绝对值) max（求最大值） int(将其他类型转为整数)float(同左)str（同左）bool(同左)hex(转换为十六进制)
print(int(0.1))
print(max(0, 0.1))
print(abs(-0.001))
print(float(111))
print(bool("0"))


# a = help()
# print(help(abs))
# pass可以用来作为占位符
class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False


# 函数的返回值和参数
# 默认参数，*args 可变参数（装到元组里边传递） ，**kw关键字参数（dict）
# 返回值其实是一个元组
# 命名关键字参数，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person1(name, age, *args, city="beijing", job="it"):
    print(name, age, args, city, job)
