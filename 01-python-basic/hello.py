import random
num = random.randint(0,100)

while True:
    guess = int(input("请输入你的数字："))
    if guess > num:
        print("你猜大了")
    elif guess < num:
        print("你猜小了")
    else:
        print("你猜对了")
        break