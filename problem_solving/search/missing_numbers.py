def missingNumbers(arr, brr):
    j=0
    res = []
    while len(arr):
        # print(arr)
        if brr[j] in arr:
            arr.remove(brr[j])
            brr.remove(brr[j])
        else:
            # res.append(brr[j])
            j+=1
    a = list(set(brr))
    a.sort()
    return a
