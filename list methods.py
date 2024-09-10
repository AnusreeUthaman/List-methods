#LIST METHODS

#append(item)
x=[3,4,5,2,1,4]
x.append(6)
print(x)#[3,4,5,2,1,4,6]

#insert(index,item)
x=[3,4,5,2,1,4]
x.insert(3,7)
print(x)#[3, 4, 5, 7, 2, 1, 4]

#remove(item)
x=[3,4,5,2,1,4]
x.remove(2)
print(x)#[3, 4, 5, 1, 4]

#pop()
x=[3,4,5,2,1,4]
x.pop(3)
print(x)#[3, 4, 5, 1, 4]

#pop(index)
x=[3,4,5,2,1,4]
x.pop(1)
print(x)#[3, 5, 2, 1, 4]


#extend
a=[1,2,3]
b=[4,5]
print(a+b)#[1,2,3,4,5]
b.extend(a)
print(b)#[4,5,1,2,3]
a.extend(b)
print(a)#[1, 2, 3, 4, 5]

#count()
x=[3,4,5,2,1,4,4]
print(x.count(4))#3(4 appears 3 times in a list)


#sort()-ascending
x=[3,4,5,2,1,4]
x.sort()
print(x)#[1, 2, 3, 4, 4, 5]

#sort(reverse=True)descending
x=[3,4,5,2,1,4]
x.sort(reverse=True)
print(x)#[5, 4, 4, 3, 2, 1]


#reverse
x=[3,4,5,2,1,4]
x.reverse()
print(x)#[4, 1, 2, 5, 4, 3]


#index
x=[3,4,5,2,1,4]
print(x.index(4))#1


      


