thing = input("请输入你要买的东西：")
money = input("请输入东西的金额：")

with open("bill1.txt","a") as file:
    file.write(f"{thing}, {money}元\n")