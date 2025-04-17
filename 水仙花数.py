number=str(input("输入一个数："))
j=0
for i in number:
    i=int(i)
    j+=i**3
if j==int(number):
    print("{number}是水仙花数")
else:
    print("{number}不是水仙花数")
