a=eval(input("输入："))
for i in range(a+1,1,-1):
    if i%17==0and i%5!=0:
       break
print(i)
