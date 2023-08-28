def ask_ok(prompt,retries=4,reminder='Try Again\n'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries-1

        if retries<0:
            raise ValueError('Invalid User Response')
        
        print(reminder)


#ask_ok('Please Enter => ')


i=10

def f(arg=i):
    arg=20
    print(arg)
f()
print(i)
'''
***name => dictionary arguements
*name => tuple type
'''

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def make_inc(n):
    return lambda x:x+n

func=make_inc(42)

func(12)
