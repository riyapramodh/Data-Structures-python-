#using list as stack
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
print(len(stack) == 0)
#to print the last element
print(stack[-1])




#when limit is not set for the stack
stack = []
def push():
    for i in range(10):
        print("enter an object :")
        n = int(input())
        stack.append(n)
        print(stack)
def pop():
    print("enter the number of times you want to perform pop:")
    N = int(input())
    if N<11:
        for i in range(N):
            if len(stack)== 0:
                print("stack is empty")
            else:
                stack.pop()
        print(stack)
    else:
        print("invalid")

print("stack updation")
while True:
    print("please enter your choice:")
    ch = int(input())
    if ch == 1:
        print("performing push operation")
        push()
    elif ch == 2:
        print("performing pop operation")
        pop()
    elif ch ==3:
        print("exit")
        break;

#if we set limit for the stack then:
stack1 = []
def push1():
    print("enter the total number of elements in the stack:")
    N = int(input())
    if len(stack1) == N:
        print("stack is full")
    else:
        print("enter the numbers to be pushed to the stack:")
        for i in range(N):
            n = int(input())
            stack1.append(n)
            print(stack1)
def pop1():
    print("enter the number of times you wanna pop:")
    a = int(input())
    for i in range(a):
        if len(stack1) == 0:
            print("stack is empty")
        else:
            stack1.pop()
    print(stack1)

while True:
    print("please choose an operation:")
    ch = int(input())
    if ch == 1:
        print("push operation")
        push1()
    elif ch ==2:
        print("pop operation")
        pop1()
    elif ch ==3:
        print("exit")
        break;
