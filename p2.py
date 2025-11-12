#1
num=[10,20]

#2
for i in range(0,5):
    print(i)

#3
l=['b','y','e',]
l[1]='p'
print(l)

#4
l=['b','y','e',]
l.append('g')
print(l)

#5
l=['b','y','e',]
l=l+['g']
print(l)

#6
l=['b','y','e',]
l.pop(1)
print(l)

#7
l=[1,5,6,4,5,2,]
l.sort()

print(l)

#8
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l.pop(2)  # remove the third element
# Remove odd elements
l = [x for x in l if x % 2 == 0]

print(l)
