#bubblesort

def swap(a, b):
    temp = a
    a = b
    b = temp

def bubblesort(A):
    for i in range(len(A) - 1):
        for j in range(len(A), i + 1):
            if A[j] < A[j - 1]:
                swap(A[j], A[j - 1])


