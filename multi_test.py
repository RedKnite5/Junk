import time
from multiprocessing import Pool

# so that iPython works
__spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

import numpy
def numpy_sin(value):
    return numpy.sin(value)

a = numpy.arange(1000000)

if __name__ == '__main__':

    pool = Pool(processes = 8)

    start = time.time()
    result = numpy.sin(a)
    end = time.time()
    print('Singled threaded {}'.format(end - start))
    start = time.time()
    result = pool.map(numpy_sin, a)
    pool.close()
    pool.join()
    end = time.time()
    print('Multithreaded {}'.format(end - start))



p = 3
s = 1000

a = [numpy.arange(s) for _ in range(10)]

if __name__ == '__main__':

    print('processes = {}'.format(p))
    print('size = {}'.format(s))

    start = time.time()
    result = numpy.sin(a)
    end = time.time()

    print('Singled threaded {}'.format(end - start))

    pool = Pool(processes = p)
    start = time.time()
    result = pool.map(numpy_sin, a)
    pool.close()
    pool.join()
    end = time.time()

    print('Multithreaded {}'.format(end - start))