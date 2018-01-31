# distutils: language = c++

from sparsehash.dense_hash_map cimport dense_hash_map
from libcpp.string cimport string


cpdef void test_access_func() except *:
    cdef dense_hash_map[string, int] d
    d.set_empty_key("")
    d["monday"] = 2

    assert d['monday'] == 2

cpdef void test_build_func() except *:
    cdef:
        dense_hash_map[int, int] d
        int i, N = 98
        int[98] array;

    d.set_empty_key(-1)
    for i in range(N):
        d[i] = i * 2
        array[i] = i * 2

    assert d.size() == 98

    for i in range(N):
        assert d[i] == array[i]

cpdef void test_del_func() except *:
    cdef:
        dense_hash_map[int, int] d
        int i, N = 98

    d.set_empty_key(-1)
    d.set_deleted_key(-2)

    for i in range(N):
        d[i] = i * 2

    assert d.size() == 98
    d.erase(95)
    assert d.size() == 97

    for i in range(N):
        if d.find(i) == d.end():
            assert i == 95

cpdef void test_has_func() except *:
    cdef:
        dense_hash_map[int, int] d
        int i, N = 98

    d.set_empty_key(-1)
    d.set_deleted_key(-2)

    for i in range(N):
        d[i] = i * 2

    assert d.find(97) != d.end()
    assert d.find(98) == d.end()
