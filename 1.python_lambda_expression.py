#Use lambda functions when an anonymous function is required for a short period of time.

x = lambda a:a+10
print(x(5))

y = lambda a,b : a*b
print(y(2,3))


def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(2)

print(mydoubler(11))
