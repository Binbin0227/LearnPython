import random
num = random.randint(0,9)
n = 0
while True:
    guess = input("请输入一个0 - 9的整数: ")
    n+=1
    if int(guess) == num:
        print(f"猜对了！你一共猜了{n}次")
        break
    elif int(guess) > num:
        print("遗憾太大了")
    elif int(guess) < num:
        print("遗憾太小了")
