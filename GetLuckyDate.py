import random
def getDate(inputNumber):
     if inputNumber==1:
         return 'It is Monday'
     elif inputNumber==2:
         return 'It is Tuesday'
     elif inputNumber==3:
         return 'It is Wednesday'
     elif inputNumber==4:
         return 'It is Thuresday'
     elif inputNumber==5:
         return 'It is Friday'
     elif inputNumber==6:
         return 'It is Satursday'
     elif inputNumber==7:
         return 'It is Sunday'

r = random.randint(1,7)
luckyDay = getDate(r)
print(luckyDay)
