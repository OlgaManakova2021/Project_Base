var1 = 'global'

def my_func():
    global var1, var2
    var1 = "local"
    print(var1)
    var2 = "two"

my_func()
print(var1)
print(var2)



