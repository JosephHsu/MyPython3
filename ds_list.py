# list 元素可以是任何的Python物件 不用事先定義其型別與大小
# tuple 只是改用()來建立 ，建立後無法改變其值 用在多重指定變數 packing unpacking (P5-27)
x = [2,"tow",[1,3]]
print(len(x))
print(x[-1]) #list的最後一個起算
print(x[0]) #list的第一個起算

print("index正數往右邊算 負數往左邊算 如果index2在index1之前會是空list")
print(x[-1:2])

print("省略index1表示從頭開始，省略index2表示到尾端")
print(x[:3])
print(x[1:])

print("copy list")
y = x[:]
print(y)

print("右邊的list新增元素")
x[len(x):] = [4,5,6]
print(x)
print("左邊的list新增元素")
x[:0] = [0,1]
print(x)
print("移除list")
x[1:-1] = []
print(x)

print("list物件的方法:insert")
z = [1,2,3]
z.insert(2,4)#在index 2之前插入4
print(z)