#记得输入冒号
def leapyear(num):
    res0=num%4
    res1=num%100
    res2=num%400
    result=(res0==0 and res1!=0) or (res2==0)
    return result
num1=int(input('Please enter the year:'))
if leapyear(num1):
    s='is'
else:
    s='Not'
print('{0} {1} a leap year.'.format(num1,s))
