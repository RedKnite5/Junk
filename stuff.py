
# stuff.py




import time

class Context(object):
    def __enter__(self):
        pass

    def __exit__(self, type, value, trace):
        print("Ending")



with Context():
    print("script")




