def balancedSums(arr):
    l=0
    r=len(arr)-1
    res='NO'
    if len(arr)==1:
        res='YES'
    else:
        while l<r:
            mid = (r+l)//2
            
            if sum(arr[:mid])==sum(arr[mid+1:]):
                res='YES'
                break
            if sum(arr[:mid])>sum(arr[mid+1:]):
                if mid==r:
                    r-=1
                else:
                    r=mid
            else:
                if l==mid:
                    l+=1
                else:
                    l=mid
    return res
