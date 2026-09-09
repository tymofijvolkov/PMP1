def fib():
    a = 1
    b = 1
    res = []
    
    for i in range(1, 26):
        if i >= 5:
            res += [a]
        a, b = b, a + b
        
    return res, len(res)
