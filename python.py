import keyword
print(keyword.kwlist)

a=None
print(a)


a=0
print(type(a))
print(bool(a))


print(bool([1.0]))  
print(bool([0]))
print(bool([0.0]))

q=3j+5
print(q)


a=6j
print(a)



'''list'''
a=[1,2,3,4,5,True,'Hello']
print(a)


a.append(6)
print(a)
popped_value = a.pop()
print("the popped vlue is:",popped_value)
print(a)

'''Tuple'''
a=(1,2,3,4,5,True,'hello' )
print(a)

'''a={'a':[10,20,30],'b':40}
print(a['a'][1][-2])'''

'''a='Hello'
print(a[2:4])
print(a[-3:-2+1])

a="Good Morning"
print(a[7:11])
print(a[7:10+1])
print(a[7:-5-6])
print(a[1:5+1:2])
print(a[-7::3])
print(a[5:3])
print(a[-2:-9:-3])


a=eval(input("enter:"))
print(a,type(a))'''

'''a=int(inputr("Enter a number:"))
if a%2==0
print('enen')
else:
print('odd')'''


'''a=eval(input("Enter a list:"))
if len(a)==5:
    print('yes')
else:
        print('no')'''

ch=input("enter:")

if  "A"<=ch<="Z":
    print('upper')
elif "a"<=ch<="z":
    print('lower')
else:
    print('not a alpha')
'''I=1
while i<=100
print(i)
i+=1'''

'''i=1
while(i<=50):
    if i%2==0:
        print(i)
    i+=1'''


'''n=int(input("Enter a number:"))
rev=0
while(n>0):
    id=n%10
    rev=rev*10+id
    n=n//10
    print("The reverse of the number is:",rev)'''


'''s=input('enter:')
out=''
for i in s:
    if"A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
print(out)'''

'''s=input('enter:')
rev=''
for i in s:
    rev=i+rev
print(rev)
'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')  
    print()'''

''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()
        ''
    
