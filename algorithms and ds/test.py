def push(stack1, stack2, x):
    stack1.append(x)


def poll(stack1, stack2):
    print(stack1[0])
    del stack1[0]

'''
def Push(x,stack1,stack2):
   
    stack1.append(x)
    
    #code here

def Pop(stack1,stack2):
    

    if len(stack1) == 0:
        return -1
    while len(stack1) > 1:
        stack2.append(stack1.pop())
    x = stack1.pop()
    while len(stack2) != 0:
        stack1.append(stack2.pop())
    return x
    
    #code here
'''

stack1 = []
stack2 = []
push(stack1, stack2, 1)
push(stack1, stack2, 2)
poll(stack1, stack2)
push(stack1, stack2, 4)
poll(stack1, stack2)
