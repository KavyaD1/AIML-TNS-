#index in tuple

my_tuple=(10,20,30)
index_of_20=my_tuple.index(20)
print("Index of 20:", index_of_20)

#count in tuple

my_tuple = (10, 20, 30)
count_of_20 = my_tuple.count(20)
print("Count of 20:", count_of_20)

#Given a tuple of numbers and a target element, find and print all indexes where the target element occurs in the tuple.

my_tuple = (10, 20, 30, 20, 40, 20, 50, 60, 20)
target = 20

indexes = []

for i in range(len(my_tuple)):
    if my_tuple[i] == target:
        indexes.append(i)

print("Indexes where target occurs:", indexes)


#Sets

my_set={1,2,3,4,5}
print("Initial Set:", my_set)
print(type(my_set))

#add
my_set={1,2,3,4,5}
my_set.add(6)
print(my_set)

#update
my_set={1,2}
my_set.update((1,2,8),[5,6,7])
print(my_set)

#remove
my_set={1,2,3,4,5}
my_set.remove(5)
print(my_set)

#discard
my_set={1,2,3,4,5}
my_set.discard(6) #won't raise error if the element not in set
print(my_set)

#my_set={1,2,3,4,5}
my_set.pop()
print(my_set)

#clear
my_set={1,2,3,4,5}
my_set.clear()
print(my_set)

#union
my_set1={1,2,3,4,5}
my_set2={1,2,6,4,8}
result=my_set1.union(my_set2)
print("Union:",result)

#intersection
my_set1={1,2,3,4,5}
my_set2={1,2,6,4,8}
result=my_set1.intersection(my_set2)
print("Intersection:",result)

#difference
my_set1={1,2,3,4,5}
my_set2={1,2,6,4,8}
result=my_set2.difference(my_set1)
print("Difference:",result)

#issubset
my_set1={1,2,3,4,5}
my_set2={1,2,3,4,5,6,7}

print("Is my_set1 subset of my_set2?", my_set1.issubset(my_set2))

#issuperset
my_set1={1,2,3,4,5}
my_set2={1,2,6,4,8}
print("Is my_set1 subset of my_set2?", my_set1.issubset(my_set2))

#remove duplicates from a list using set
numbers = {1, 2, 3, 2, 4, 1, 5}   
result = list(set(numbers))  
print("List after removing duplicates:", result)

