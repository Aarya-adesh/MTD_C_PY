#python program to print the number from m to n (m<n) with an increment of p 

m= int(input('enter the m value (start value ):'))
n= int(input('enter the n value (end value ):'))
p= int(input('enter the p value p(increment):'))

i=m 
while i<n:
    print(f'{i}\n')
    i=i+p