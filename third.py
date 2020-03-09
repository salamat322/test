def fibo(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(50))


