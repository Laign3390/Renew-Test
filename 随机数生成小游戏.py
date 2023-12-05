#记得输冒号
'''随机生成10个0~100之间的整数，要求不能有重复值。
   用户输入一个整数x，在10个随机整数中查找x，如果找到，则提示找到；
   如果未找到，则提示重新输入，用户最多只能查找5次，否则提示“游戏结束”。
   最后输出10个随机整数。
  （提示：可利用列表。要求生成随机数和查找功能分别由自定义函数实现。）'''
from random import*
def rnum(a):
    while len(a)<=10:
        n=randint(0,100)
        for i in a:
            if i==n:
                break
        else:
            a.append(n)
def search(a):
    for i in range(5):
        b=int(input('Please enter a number:'))
        if b in a:
            print('Find already,congratulations!')
            break
        else:
            print('Not find,please enter again.')
    else:
        print('Game over !')
list3=[]
rnum(list3)
search(list3)
print(list3)
