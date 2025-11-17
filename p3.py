#1
birthday = {
    "A": "2/11/2020",
    "B": "5/4/2000",
    "C": "6/6/2005"
}
print(birthday)

#2
data={
    "name":"A",
    "age":25,
    "city":"USA"
}
print(data)
print(data["name"])
print(data["age"])
print(data["city"])

#3
p={"r":1,"q":2,"s":3}
print(p)
p["r"]=4 #update
print(p)

#4
p = {True: 1, False: 0}
print(p)

p[True] = 5
print(p)

#5
p={{"name"}:1,"q":2,"s":3}
print(p)
p["r"]=4
print(p)

#5
emp = {}   

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    emp[name] = number    

print("\nEmployee Details:")
for name, number in emp.items():
    print(name, ":", number)

#6
emp = {}
n = int(input("Enter no of employees: "))

for i in range(n):
    name = input("Enter emp name: ")
    no = int(input("Enter emp no: "))
    emp[name] = no      # store in dictionary

for name, no in emp.items():
    print(name, ":", no)
