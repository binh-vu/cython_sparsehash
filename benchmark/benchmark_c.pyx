from sparsehash.dense_hash_map cimport dense_hash_map
from sparsehash.dense_hash_set cimport dense_hash_set


cpdef void test_build_dict_c(int N):
    cdef:
        dense_hash_map[int, int] d
        int i

    d.set_empty_key(-1)
    for i in range(N):
        d[i] = i * 2


cpdef void test_build_dict(int N):
    cdef:
        dict d = {}
        int i

    for i in range(N):
        d[i] = i * 2


cpdef void test_access_dict_c(int N, int M):
    cdef:
        dense_hash_map[int, int] d
        int i, val, j = 0

    d.set_empty_key(-1)
    for i in range(N):
        d[i] = i * 2

    for i in range(M):
        val = d[j] * 2
        j += 1
        if j >= N:
            j = 0



cpdef void test_access_dict(int N, int M):
    cdef:
        dict d = {}
        int i, val, j = 0

    for i in range(N):
        d[i] = i * 2

    for i in range(M):
        val = d[j] * 2
        j += 1
        if j >= N:
            j = 0


cpdef void test_build_set(int N):
    cdef:
        set c = set()
        int i

    for i in range(N):
        c.add(i)


cpdef void test_access_set(int N, int M):
    cdef:
        set c = set()
        int i, count = 0

    for i in range(N):
        c.add(i)

    for i in range(M):
        if i in c:
            count += 1


cpdef void test_build_set_c(int N):
    cdef:
        dense_hash_set[int] c
        int i

    c.set_empty_key(-1)
    for i in range(N):
        c.insert(i)


cpdef void test_access_set_c(int N, int M):
    cdef:
        dense_hash_set[int] c
        int i, count = 0

    c.set_empty_key(-1)
    for i in range(N):
        c.insert(i)

    for i in range(M):
        if c.find(i) != c.end():
            count += 1
