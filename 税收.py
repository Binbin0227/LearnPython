money=eval(input("收入:"))
marry=eval(input("婚姻（未婚：0 已婚1）输入数字:"))
if marry==0:
    if 0<money<=8000:
        charge=money*0.1
    elif 8000<money<=32000:
        charge=800+(money-8000)*0.15
    elif 32000<money:
        charge=4400+(money-32000)*0.25
elif marry==1:
    if 0<money<=16000:
        charge=money*0.1
    elif 16000<money<=64000:
        charge=1600+(money-16000)*0.15
    elif 64000<money:
        charge=8800+(money-64000)*0.25
print(f"税收：{charge}")
