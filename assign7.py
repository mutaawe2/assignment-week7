#qn2
from signal import default_int_handler


def snail_climb(depth):
    print(depth//5 + "days")

#qn3
def myMax(list1):
 
    
    max = list1[0]

    for x in list1:
        if x > max:
            max = x
 
    return max
 

list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))

#qn4
phrase = input("Type in: ")
phrase = list(phrase)

u, l = 0, 0
for i in phrase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER:", u)
print("lower:", l)
#qn six

class student:
    def __init__(self, name, age, streem ):
        self.name = name 
        self.age  =age 
        self.streem=streem

student1 = student("ali",27 ,"G")
print(dir(student))
#7

class stack:
    def __init__(self):
       self.stack =list()
    def isEmpty(self):
        return len(self.stack) ==0
    def push(self, data):
        self.stack.append(data)
    def peek(self):
        return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return("stack is empty. stack underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    def show(self):
        return self.stack


        