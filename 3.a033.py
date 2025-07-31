MAX_SIZE = 5
stack = []
top = -1



def push (book_title):
    global top
    if top >=MAX_SIZE -1:
        print("stack overflow! cannot push more books.")
    else:
        top += 1
        stack.append(book_title)
        print(f"book'{book_title}'pushed onto the stack.")

def pop():
    global top
    if top ==-1:
        print("stack underflow!cannot pop any books.")
    else:
        removed_book=stack.pop()
        print(f"book'{removed_book}'popped from the stack")
        top-=1

def peek():
    if top ==-1:
        print("stack is empty.no book to peek")
    else:
        print(f"top book on the stack:'{stack[top]}'") 

def display():
    if top ==-1:
        print("stack is empty")
    else:
        print("book in stack (top to bottom):")
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")


push("harry potter")
push("the hobbit")
push("365 days")
push("the summer")
push("love story")
push("dark sight")


display()
peek()
pop()
pop()
display()
peek()

        
