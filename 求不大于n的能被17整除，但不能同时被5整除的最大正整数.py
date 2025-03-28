n=eval(input("输入："))
for i in range(n+1,1,-1):
    if i%17==0 and i%5!=0:
       break
print(i)
