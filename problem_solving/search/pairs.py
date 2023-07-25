def pairs(k, arr):
    c= 0
    b =set(arr)
    for i in b:
        if i+k in b:
            c+=1
    return c
