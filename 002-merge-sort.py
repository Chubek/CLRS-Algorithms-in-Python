#merge sort

def merge_sort(A, p, q, r):
    n_prime = q - p + 1
    n_second = r - q
    L = [x for x in range(n_prime + 1)]
    R = [y for y in range(n_second + 1)]
    
    for i in range(n_prime):
        L[i] = A[p + i - 1]
    
    for j in range(n_second):
        R[j] = A[q + j]

    L[n_prime] = float("inf")
    R[n_second] = float("inf")

    i = 0
    j = 0

    for k in range(p, r):
        if i < len(L) and i < len(R) and L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A



A = [2, 4, 5, 7, 8, 6, 9, 1]

print(merge_sort(A, 0, 3, 7))




