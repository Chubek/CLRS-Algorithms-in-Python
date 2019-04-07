#bubblesort

def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

    return A

def bubblesort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A = swap(A, j, j - 1)

    return A



A = [5, 2, 1, 6, 3, 6, 4]

print(bubblesort(A))