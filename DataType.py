# -*- coding: utf-8 -*-
"""
數值型態 ：
    整數 int ,Py3之後就不再有分int ,long
    浮點數 float
    布林 bool , True and False(None,0,0.0,0j,'' 空字串,() tuple,[] list,{} dict)
    複數 complex , a+bj
"""
print("===============以下分別為10的十進位,二進位,八進位,十六進位")
print(10)
print(0b1010)
print(0o12)
print(0xA)

print("===============驗證某個值得型態，可type()")
print(type(10))
print(type(0xA))

print("===============轉換型態，可用int(),float(),bool()")
print(int('10'))
print(int(True))
print(int(False))
print(int(3.1415926))

print(float('3.14152936'))

print(bool(1))

print("===============字串,習慣上用單引號，如果字串當中有單引號使用雙引號")
print('\\t')
#raw string
print(r'\t')
print('It is a string')
print("It's a String")
print('''It will show everything you input including line break
        Here is new line!''')





