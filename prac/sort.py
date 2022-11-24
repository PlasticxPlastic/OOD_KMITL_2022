#Bubble Sort
def bubble(l):
    for last in range(len(l)-1,0,-1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break
    return l

#bubble Sort Recursive
def bubbleSortRecursive(l):
    if len(l) <= 1:
        return l

    if len(l) == 2:
        return l if l[0] < l[1] else [l[1], l[0]]

    a, b = l[0], l[1]
    bs = l[2:]
    res = []

    if a < b:
        res = [a] + bubbleSortRecursive([b] + bs)
    else:
        res = [b] + bubbleSortRecursive([a] + bs)
    return bubbleSortRecursive(res[:-1]) + res[-1:]

#Selection Sort
def selection(l):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1, last + 1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = l[biggest_i], l[last]
        return l

#Selection Sort Recursive

def minIndex( a, i, j):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)

def SelectionSortRecur(l,index = 0):
    if index == len(l):
        return 0
    k = minIndex(l, index, len(l)-1)
    if k != index:
        l[k], l[index] = l[index], l[k]
    SelectionSortRecur(l, index + 1)
    return l

#insertion Sort
def insertionSort(l):
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return l

#insertion Sort Recursive

def insertionSortRecursive(l, n):
    if n < 1:
        return
    insertionSortRecursive(l,n-1)
    last = l[n-1]
    j = n-2
    while (j >= 0 and l[j] > last):
        l[j+1] = l[j]
        j = j-1
    l[j+1] = last
    return l

#Shell Sort
def Shell(l, dIncrements):
    for inc in dIncrements:
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle < l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    return l
                    break
    return l

#merge sort
def mergeSort(l, left, right):
    center = (left + right)//2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
        merge(l,left,center + 1, right)
    return l

def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1

    for ele in result:
        l[start] = ele
        start += 1
        if start > rightEnd:
            break
    print(result)

#Quick Sort

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)
    return array




l = [5,6,2,3,0,1,4]
k = [2,4,6,1,2,4,1,2,4]
n = len(l)
dIncrements = [5,3,1]
print("Bubble Sort")
print(bubble(l))
print()
print("Bubble Sort Recursive")
print(bubbleSortRecursive(l))
print()
print("selection sort")
print(selection(l))
print()
print("selection sort recursive")
print(SelectionSortRecur(l))
print()
print("insertion sort")
print(insertionSort(l))
print()
print("insertion sort recursive")
print(insertionSortRecursive(l,n))
print()
print("shell sort")
print(Shell(l,dIncrements))
print()
print("merge sort")
print(mergeSort(k,0,len(k) - 1))
print()
print("Quick Sort")
print(quickSort(l,0,len(l)-1))
print()


