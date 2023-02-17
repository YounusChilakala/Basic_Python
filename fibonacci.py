a=0
b=1
i=0
n=int(input('enter your value'))
print(a)
print(b)
while i<n+1:
    c=a+b
    a,b=b,c          
    i+=1
    print(c)

#explanation
#0 1 1 2 3 5 8
#a b c
#  a b c
#    a b c
 #step 1: base nums are added a=0,b=1---> c=a+b=1
 #step 2: assign those as new base nums---> new a is b(1 earlier) and the new b is c( the sum)