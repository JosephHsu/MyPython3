name = input("How are you ?")
print('Hello World')
print(name)
#註解 This line of code does nothing
# ctrl K C 加上註解。 ctrl K U 移除註解
# terminal 過多可以cls
# 字串要用單引或雙引都沒差，只要保持一致性就好
print('Give a blank line\n New Line')
print("It's my life !")

# combine string withs +
firstName = "JOSEPH"
lastName=  "Hsu"
print('Hello~' + firstName.capitalize() +'   '+lastName)

# 用 tab 來確定要選用的提示清單
# string formatting
result = 'Hello~{} {}'.format(firstName,lastName)
print(result)
#only available in python3
print(f'Hello,{firstName} {lastName}')