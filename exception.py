x = 2
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
finally:
    print('Done !')