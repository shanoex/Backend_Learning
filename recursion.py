def add_one(n):
    if(n>=9):
        return n+1
    total=n+1
    print(total)
    return add_one(total)
print(add_one(0))
    