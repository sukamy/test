total=0
count=0
average=0
user_input=input("give me your num,I can return the average(quit until input \"exit\"):")
#print(type(user_input))  # class str  need translation
while user_input!="exit":
    total+=float(user_input)
    count+=1
    user_input = input("give me your num,I can return the average(quit until input \"exit\"):")
if count==0:
    average="no input"
else:
    average=total/count

print(f"the average is:+ {average}" )