# Optimization

- Well chosen simulation parameters are the first (and can be the most important) step in reducing run time
- Use the Anaconda distribution to get free access to the [Intel MKL](https://software.intel.com/en-us/mkl), which 
    - will automatically [vectorize](https://en.wikipedia.org/wiki/Vector_processor) many numpy operations
    - can be [configured](https://docs.anaconda.com/mkl-service/) to parallelize some operations across multiple CPU cores

- Consider using [numexpr](https://github.com/pydata/numexpr) to evaluate compound expressions efficiently

- If your system contains [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) (a matrix in which most elements are zero), use one of [scipy.sparse’s](https://docs.scipy.org/doc/scipy/reference/sparse.html) sparse matrix representations (e.g. csr_matrix)

- Use a profiler ([cProfile](https://docs.python.org/2/library/profile.html) in Python) to identify hot-spots in your code

- Consider modifying / rewriting those sections of your Python code to work with either
    - [NUMBA](http://numba.pydata.org/): this might be preferable, because it works on pure Python (though doesn’t [support all Numpy functions](http://numba.pydata.org/numba-doc/latest/reference/numpysupported.html) in the fast [‘nopython’](http://numba.pydata.org/numba-doc/latest/user/5minguide.html#what-is-nopython-mode) mode). Also supports [automatic parallelization](http://numba.pydata.org/numba-doc/latest/user/jit.html#parallel) across CPU cores, and even execution on a [GPU](http://numba.pydata.org/numba-doc/latest/user/5minguide.html#gpu-targets). Or,
    - [Cython](https://cython.readthedocs.io/en/latest/): popular way to write high-performance Python-like code. Requires changing your code so it is no longer runnable on the default Python interpreter if you want native performance.

- An alternative to writing your numerical code in Python, write it in C instead and utilize the Intel MKL to vectorize all your linear algebra.
    - Initialize your simulation parameters, and handle/process your data in Python. Only the simulation is run in C. You can call your C code using Python extension modules, ctypes, or cffi.
    - Use [OpenMP](https://en.wikipedia.org/wiki/OpenMP) to decorate C code with hints to automatically execute across multiple CPUs.
    - For very large numerical simulators (e.g. cluster-scale), use [Open MPI](https://en.wikipedia.org/wiki/Open_MPI) to manually implement a distributed simulator, appropriate for running on compute clusters.

Further reading:

[Interfacing with C from Python](https://scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html)

[Extending Python with C or C++](https://docs.python.org/2/extending/extending.html)

[Building C and C++ Extensions with distutils](https://docs.python.org/2/extending/building.html)

[Cython: Working with Numpy](https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html)
