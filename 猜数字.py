import random
num = random.randint(0,9)
n = 0
while True:
    guess = input("输入")
    n+=1
    if guess == num:
             ___________
        print("猜中")
    elif guess<num:
              print(“遗憾太大了”)
    elif guess>num:
              print(“遗憾太小了”)
