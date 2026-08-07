question = input("请输入问题：")
name = input("请输入名字：")
user = {
    "name": name,
    "question": question
    
}

response = {
    "answer": "Python是一种简单易学的编程语言"
}

print(f"用户{user['name']}的问题是{user['question']}")
print(f"ai回答：{response['answer']}")