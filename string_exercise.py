'''
#programe to calculate length of string
s = 'string'
print(len(s))

def string_lenght(str1):
    count = 0
    for char in str1:
        count+=1
    return count
print(string_lenght('my hope is alive'))

def str_len(str2):
    a = 0
    while a<len(str2):
        a+=1
    return a
print(str_len('python'))

#count words in string
string1 = input('enter string')
words = []
words = string1.split()
frequency = [words.count(i) for i in words]
print(words)
print(frequency)
dict1 = dict(zip(words,frequency))
print(dict1)

s1 = input('enter string')
character = input('char name')
print(character)
print(s1.count(character))

s1 = input('enter string')
dict1 = {}
for i in s1:
    dict1[i] = s1.count(i)
print(dict1)

list1 = s1.split()
dict2 = {}
for i in list1:
    dict2[i] = list1.count(i)
print(dict2)

def char_freuency(str1):
    dict1 = {}
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1
print(char_freuency('hello'))

def end_char(str1):
    if len(str1)>2:
        L = str1[0:2] + str1[-2:]
    else:
        L = 'empty'
    print(L)

R = input('enter string')
end_char(R)

s1 = 'hello'
dict1 = {}
for i in s1:
    dict1[i] = s1.count(i)
print(dict1

def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char+str1[1:]
    return str1
print(change_char('hight'))

str1 = 'abc'
str2 = 'xyz'
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]
print(new_str1+' '+new_str2)


str1 = input('enter string')
if len(str1)>=3:
    if str1[-3:] == 'ing':
        a = str1 + 'ly'
        print(a)
    else:
        a = str1 + 'ing'
        print(a)
else:
    print(str1)



L = []
n = int(input('how many words?'))
for i in range(n):
    word = input('enter word')
    L.append(word)
print(L)



L = []
n = int(input('enter number of word'))
i = 0
while i<n:
    word = input('enter word')
    L.append(word)
    i+=1
print(L)


L = []

while True:
    word = input('enter object')
    L.append(word)
    choice = input('want to stop press "s", if not then other key')
    if choice == 's':
        break
print(L)
'''
