#sequential search
def seq_srch(arr,ele):
    pos=0
    found=False
    stopped=False
    while pos<len(arr) and not found and not stopped:
        if arr[pos]==ele:
            found= True
        else:
            if arr[pos]>ele:
                stopped=True
            else:
                pos+=1
    return found

arr=[1,2,3,5]
print(seq_srch(arr,4))


def binarysearch(arr,ele):
    low=0
    high=len(arr)-1
    found=False
    while low<=high and found== False:
        mid = (low+high)//2
        if arr[mid]==ele:
             found= True
        elif ele>arr[mid]:
            low= mid+1
        else:
            high=mid-1
    return found

arr=[1,3,4,5,7,8,9,11,12,13]
print(binarysearch(arr,4))

def rec_binarysearch(arr,ele):
    if len(arr)==0:
        return False
    else:
        mid=len(arr)//2
        if arr[mid]==ele:
            return True
        elif arr[mid]>ele:
            return rec_binarysearch(arr[:mid],ele)
        else:
            return rec_binarysearch(arr[mid+1:],ele)

arr=[1,3,4,5,7,8,9,11,12,13]
print(rec_binarysearch(arr,10))

#insertion sort
def insertion_sort(arr):
    for i in range (1,len(arr)):
        current=arr[i]
        position = i
        while position>0 and arr[position-1]>current:
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=current
arr=[2,3,4,8,7,5,6,4,3,2]
insertion_sort(arr)
print(arr)

#quick sort
def quick_sort(arr):
    quick_sort_help(arr,0,len(arr)-1)
def quick_sort_help(arr,first,last):
    if first<last:
        splitpoint= partition(arr,first,last)
        quick_sort_help(arr, first, splitpoint - 1)
        quick_sort_help(arr, splitpoint + 1, last)

def partition(arr,first,last):
    pivot_value=arr[first]
    left_mark=first+1
    right_mark=last
    done=False
    while not done:
        while left_mark<=right_mark and arr[left_mark]<=pivot_value:
            left_mark +=1
        while right_mark>= left_mark and arr[right_mark]>=pivot_value:
            right_mark -=1
        if right_mark<left_mark:
            done=True
        else:
            temp=arr[left_mark]
            arr[left_mark]=arr[right_mark]
            arr[right_mark]=temp
    tmp=arr[first]
    arr[first]=arr[right_mark]
    arr[right_mark]=tmp
    return right_mark
arr=[3,6,5,4,8,7,6,9]
(quick_sort(arr))
print(arr)
print("\n \n")





