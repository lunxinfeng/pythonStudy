from builtins import str

message = "Hello 'Python'\"\""
print(message)
message = " Hello world "
print(message.title())  # 首字母大写
print(message.lower())  # 转换小写
print(message.upper())  # 转换大写
print(message.count("o"))  # 字符计数
print(message.strip())  # 去首尾空格
print(message.lstrip())  # 去开头空格
print(message.rstrip())  # 去结尾空格
print(message.__len__())  # 字符串长度

print(2 ** 3)  # 8
print(3 / 2)  # 1.5
print(4 / 3)  # 1.3333333333333333
# print("Hello " + 213)  # TypeError: must be str, not int
print("Hello " + str(213))  # Hello 213

names = ["Allen", "Toto", 123]
print(names)  # ['Allen', 'Toto', 123]
print(names[1])  # Toto
print(names[-1])  # 123
names[2] = 456
print(names)  # ['Allen', 'Toto', 456]
names.append(True)
print(names)  # ['Allen', 'Toto', 456, True]
names.insert(1, 123)
print(names)  # ['Allen', 123, 'Toto', 456, True]
del names[-1]
print(names)  # ['Allen', 123, 'Toto', 456]
test = names.pop(-1)
print(names)  # ['Allen', 123, 'Toto']
print(test)  # 456
names.remove("Allen")
print(names)  # [123, 'Toto']

names = ["Allen", "Toto", "Lili"]
names.sort()
print(names)  # ['Allen', 'Lili', 'Toto']
names.sort(reverse=True)
print(names)  # ['Toto', 'Lili', 'Allen']
print(sorted(names))  # ['Allen', 'Lili', 'Toto']
print(names)  # ['Toto', 'Lili', 'Allen']

names = ["Allen", "Toto", "Lili"]
for item in names:  # 注意最后有个冒号,代码块需要缩进
    print(item)

nums = list(range(1, 6))  # 创建数值列表
print(nums)  # [1, 2, 3, 4, 5]
# range还支持步数
nums = list(range(1, 6, 2))  # [1, 3, 5]
print(nums)

nums = list()
for item in range(1, 6):
    nums.append(item ** item)
print(nums)  # [1, 4, 27, 256, 3125]

# 列表解析的格式为[表达式 + for循环]
nums = [item ** item for item in range(1, 6)]
print(nums)  # [1, 4, 27, 256, 3125]

nums = list(range(1, 11))
# 实际上是从索引1到4
print(nums[1:5])  # [2, 3, 4, 5]
# 没有指定开始索引会默认从0开始  没指定结束索引会默认到列表最后一个元素结束
print(nums[:5])  # [1, 2, 3, 4, 5]
print(nums[5:])  # [6, 7, 8, 9, 10]
print(nums[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 也支持负索引
print(nums[-3:])  # [8, 9, 10]

# 这样相当于将变量nums和nums_2都关联到了同一个列表，不是复制
nums = [1, 2, 3]
nums_2 = nums
nums_2.append(4)
print(nums_2)  # [1, 2, 3, 4]
print(nums)  # [1, 2, 3, 4]

# 可以用切片来达到复制列表的目的
nums = [1, 2, 3]
nums_2 = nums[:]
nums_2.append(4)
print(nums_2)  # [1, 2, 3, 4]
print(nums)  # [1, 2, 3]

# 元组：不可变的列表
nums = (1, 2, 3)
print(nums)  # (1, 2, 3)
print(nums[-2:])  # (2, 3)

a = "a"
b = "A"
if a == b:  # a.lower() == b.lower()
    print("a == b")
elif a.lower() == b.lower():
    print("a.lower() == b.lower()")
else:
    print(False)

nums = [1, 2, 3]
nums_2 = [3, 4, 5]
if (3 in nums) and (3 not in nums_2):  # False
    print(True)
else:
    print(False)

nums = []
a = "a"
if nums:  # a
    print("nums")
elif a:
    print("a")
else:
    print(False)

student = {"name": "Allen", "age": 15}
print(student["name"])  # Allen
student["name"] = "Lili"
print(student)  # {'name': 'Lili', 'age': 15}
student["address"] = "ChangSha"
print(student)  # {'name': 'Lili', 'age': 15, 'address': 'ChangSha'}
del student["address"]
print(student)  # {'name': 'Lili', 'age': 15}

student = {'name': 'Lili', 'age': 15, 'address': 'ChangSha'}
for k, v in student.items():
    print(str(k) + ":" + str(v))

for k in student.keys():  # 遍历字典时会默认遍历key，因此等效于 for k in student:
    print(k)

for v in set(student.values()):  # 如果需要去重的话，可以使用集合set，类似于列表，但每个元素都是独一无二的
    print(v)

nums = [1, 1, 1, 1, 2, 2, 1, 3]
while 1 in nums:
    nums.remove(1)
print(nums)  # [2, 2, 3]


# def print_hello():
#     """打招呼"""
#     print("Hello")


# print_hello()  # Hello


def print_hello(name, age="15"):
    """打招呼"""
    print("你好，我叫" + str(name) + "，" + str(age) + "岁")


print_hello("李狗蛋", "12")  # 你好，我叫李狗蛋，12岁
print_hello("12", "李狗蛋")  # 你好，我叫12，李狗蛋岁
print_hello(age="12", name="李狗蛋")  # 你好，我叫李狗蛋，12岁
# 形参可以有默认值，相当于简化了java中的方法的多态
print_hello("李狗蛋")  # 你好，我叫李狗蛋，15岁


def get_list(list):
    """测试"""
    list[0] = 2
    return list


a = [1, 2]
print(get_list(a))  # [2, 2]
print(a)  # [2, 2]
a = [1, 2]
print(get_list(a[:]))  # [2, 2]
print(a)  # [1, 2]


def muti(*name):  # 形参名*name 中的星号让Python创建一个名为name 的空元组，并将收到的所有值都封装到这个元组中。
    print(name)


muti("a")  # ('a',)
muti("a", "b", "c")  # ('a', 'b', 'c')


def person(name, age, **other):  # 形参名**other 中的星号让Python创建一个名为other 的空字典，并将收到的所有键值对都封装到这个字典中。
    p = {"name": name, "age": age}
    for k, v in other.items():
        p[k] = v
    print(other)


person("Allen", 15, sex="man", address="ChangSha")  # {'name': 'Allen', 'age': 15, 'sex': 'man', 'address': 'ChangSha'}


class Person:
    """测试类"""

    def __init__(self, name, age=15, sex="man"):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = ""
        print("person " + name + " init")

    def walk(self):
        print(self.name + " can walk.")

    def run(self):
        self.walk()
        print(self.name + " can run too.")


person = Person("Allen")  # person Allen init
person.run()  # Allen can walk.  Allen can run too.


class Student(Person):  # Student继承于Person
    def __init__(self, name):  # 子类的__init__方法需要接收父类的所有参数，有默认值的可以不传，会取默认值
        super().__init__(name)  # 子类继承父类的所有属性和方法

    def walk(self):  # 重写父类方法
        print("override function.")

    def get_teacher(self, teacher_name):  # 子类的自定义方法
        print(self.name + "'s teacher is " + teacher_name)


student = Student("Allen")  # person Allen init
student.get_teacher("Lili")  # Allen's teacher is Lili
student.walk()  # override function.

with open("file_io_test") as file:  # 关键字with 在不再需要访问文件后适时将其关闭。
    print(file.read())  # read()可以接收一个int参数，表示读取的字节数，传-1表示读取全部，默认值为-1
with open("file_io_test") as file:
    print(file.readable())  # readable()是否可读，返回一个布尔值
with open("file_io_test") as file:
    print(file.readline())  # abcdefg 行末尾有一个换行符
    print(file.readline())  # hijklmn
with open("file_io_test") as file:
    print(file.readlines())  # ['abcdefg\n', 'hijklmn\n', 'opq\n', 'rst\n', 'uvw\n', 'xyz']
with open("file_io_test") as file:
    for line in file:  # 等同于line = file.readline()
        print(line)

with open("file_write_test", mode="w+") as file:  # w换成a后可以附加到文件中，不会覆盖
    file.write("456")  # 写入456
    print(file.readable())  # True


def divide(a, b):
    """除法运算"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print(result)
    finally:
        print("运行完毕")


divide(1, 0)  # 除数不能为0  运行完毕
divide(1, 5)  # 0.2  运行完毕

import json

nums = [1, 2, 3, 4, 5]
with open("jsonTest.json", "w") as file:
    json.dump(nums, file)  # 写入文件，接收一个内容对象和文件对象

with open("jsonTest.json") as file:
    result = json.load(file)
    print(result)

# from PyQt5.QtWidgets import QApplication, QMainWindow
# from untitled import *
# import sys
#
# if __name__ == '__main__':
#     '''
#     主函数
#     '''
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())

# import this
