x = 10

def func():
    global x
    y = 20
    def func1():
        nonlocal y
        print(x + y)
    func1()



func()
