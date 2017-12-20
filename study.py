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
# import this
