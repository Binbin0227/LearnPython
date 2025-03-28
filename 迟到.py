a=eval(input("输入迟到次数:"))
if a==0:
    print("处罚措施：无")
elif a<=3:
    print("处罚措施：书面")
elif a<=5:
    print("处罚措施：扣款200元")
elif a>5:
    print("处罚措施：停职检查")
