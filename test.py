import math

print("Hello")
print("Let\'s go")
print("""君不见黄河之水天上来
奔流到海不复回
君不见高堂明镜悲白发
早如青丝暮成雪
""")
print(math.sin(1))

"""
s=input("how old are you:")
n=int(s)+10
print("ten years later,you will be "+str(n)+" years old")
"""

if True:
    print("right")

num_list = [1, 2, 10, 5]
print(list[1])
q = "hello"
print(q.upper())
num_list.append(100)
num_list.remove(2)
print(sorted(num_list))
print(num_list[1])

contacts = {("sura", 11): "11111",
            ("srma", 22): "22222"}
print(("sura", 11) in contacts)
print(contacts[("sura", 11)])
contacts["sunakoy", 112] = "158745"
print(contacts["sunakoy", 112])
del contacts[("sura", 11)]
print(len(contacts))

temperature_list = [34, 35, 2, 5, 6, 2, 7, 434, 22]
for tem in temperature_list:
    if tem > 38:
        print("shit!")
    else:
        print("My god!")

# 示例字典
my_dict = {"name": "sunakoy",
           "age": 10,
           "home": "street 1"}
for w in my_dict.keys():
    print(w)
for value in my_dict.values():
    print(value)
for first, second in my_dict.items():
    print(f"{first} : {second}")

for i in range(2):
    print(i)
print("\n")
for i in range(1, 3):
    print(i)
print("\n")
for i in range(1, 6, 2):
    print(i)
print("\n")
for i in range(5, 1, -2):
    print(i)
total = 0
for i in range(1, 101):
    total += i
print(total)

print((lambda num1, num2: num1 + num2)(2, 3))  #匿名函数lamdba

url = "https://localhost:8089"
print(url.removeprefix("https://"))

go_name = "surama"
print(go_name.upper())
print(go_name.lower())
print(go_name.title())

go_name = '\t\nsurama\t\n'
print(go_name.lstrip())
print(go_name.rstrip())
print(go_name.strip())

file = "python_note.txt"
print(file.removesuffix('.txt'))
#
# import this
# print(this.d)

letters = ['lihua', 'wangming', 'qinla']
print(letters[-1])                                 # 最后一个列表元素表示为-1也可 倒数第二表示为-2也可 以此类推

i = 0
while i < len(letters):
    print(letters[i])
    i += 1

letters.remove('lihua')
print(letters)

list = [value ** 2 for value in range(1, 11)]
print(list)

num_list = [value for value in range(1, 1_000_001)]
print(sum(num_list))
print(min(num_list))
print(max(num_list))

cube_list = [value ** 3 for value in range(1, 11)]
print(cube_list)

print(cube_list[-2:])
print(cube_list[2:])
print(cube_list[1:7:2])

my_food = ['pizza', 'chololate', 'apple']
friend_food = my_food[:]
print(friend_food)

food = ('pizza', 'banana')

for food in food:
    print(food)

alien_0 = {
    'color': 'green',
    'num': 10,
    #'color_1': 'green',
}

sorted(alien_0.keys())  #字典没有sort永久排序，只有临时排序
for color in set(alien_0.values()):       #set集合让值独一无二，不会重复出现
    print(color)




