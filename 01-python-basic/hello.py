try:
    num = int(input("请输入数字："))
    print(num)

except ValueError:
    print("输入错误")

finally:
    print("程序运行结束")