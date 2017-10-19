
import timeit
#the first version of Fibonacci
def fib1(n):
    if n <= 1:
        return n
    return fib1(n-1) + fib1(n-2)

#the second version of Fibonacci
def fib2 (n):
    if n <= 1:
        return n;
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[-2] + arr[-1])
    return arr[-1]

#the third version of Fibonacci
def fib3(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            b, a = a+b, b
        return b


starttime = timeit.default_timer()
print('first algorithm :', fib1(20))
endtime = timeit.default_timer()
print((endtime - starttime), '\n')

starttime = timeit.default_timer()
print('first algorithm :', fib2(2000))
endtime = timeit.default_timer()
print((endtime - starttime), '\n')

starttime = timeit.default_timer()
print('first algorithm :', fib3(20000))
endtime = timeit.default_timer()
print((endtime - starttime), '\n')
