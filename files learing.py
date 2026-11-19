# 正确：加 r，原始字符串，不转义 \
# f = open(r"F:\py learining flie\test\test.txt", "r", encoding="utf-8")


# line=f.readline()             #readline()每次调用都会让文本向下一行！！
# while line !="":
#     print(line)
#     line=f.readline()


# lines=f.readlines()             #readlines()不会丢失第一行，将lines看为列表 lines[0]是第一行
# for line in lines:
#     print(line,end="")

# for line in f.readlines():
#     print(line,end="")

# f.close()

with open(r"F:\py learining flie\test\test.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
    file.write("GGG")
