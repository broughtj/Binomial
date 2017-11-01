from cmath cimport pow

cdef double choose(double n, double k):
    cdef int i
    cdef int mn
    cdef int mx
    cdef double value

    if k < n - k:
        mn = k
        mx = n - k
    else
        mn = n - k
        mx = k

    if mn < 0:
        value = 0.0
    elif mn == 0:
        value = 1.0
    else
        value = <double>(mx + 1)

        for i in range(2, mn + 1):
            value = (value * <double>(mx + i)) / (<double>(i))

    return value



