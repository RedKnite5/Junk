#  numpy_stuff.py


def info(obj, depth=1):
    attrs = dir(obj)
    
    dictionary = {}
    for i in attrs:
        if i.startswith("__") and i.endswith("__"):
            if i == "__doc__":
                dictionary[i] = getattr(obj, i)
        elif "object at 0x" in str(getattr(obj, i)):
            if depth<3:
                dictionary[i] = info(getattr(obj, i), depth+1)
            else:
                dictionary[i] = ...
        else:
            dictionary[i] = getattr(obj, i)
    
    iteration = None
    try:
        iteration = tuple([info(i) for i in obj])
    except:
        pass
    
    if iteration:
        return obj, iteration, dictionary
    else:
        return obj, dictionary



if __name__ == "__main__":
    import numpy as np
    from pprint import pprint
    
    def func(var=1):
        print(var)
        return 2
    
    with open("info.txt", "w+") as file:
        pprint(info(func.__code__), file)
