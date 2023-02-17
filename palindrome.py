#For numbers

num=int(input('Enter a number '))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print('Palindrome')
else:
    print('Not a palindrome')

#For text
    
val=input('Enter text ')
rev=val[::-1]
if rev==val:
    print('Palindrome')
else:
    print('Not a palindrome')
