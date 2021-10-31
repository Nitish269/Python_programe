#sum of digit present in number
#num =int(input('enter number='))
def digit_sum(num):
    sum = 0
    while (num != 0):
        a = num % 10
        sum = sum + a
        num = num // 10
    return sum

def ams_num(num):
    n = len(str(num))
    result = 0
    while(num!=0):
        a = num%10
        a = a**n
        result = result+a
        num = num//10
    if (num == result):
        print('number is amstrong',result)
    else:
        print('number is not amstrong',result)

x = int(input('enter number to check is it amstrong or not'))
print('sum of digit in number',digit_sum(x))
ams_num(x)