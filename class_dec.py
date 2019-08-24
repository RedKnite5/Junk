# class_dec.py


def implement_common_functionality(cls_outer=None, *, attr=None, override=False):
    '''
    Decorator factory. This should be given an attribute to rederect all the
    dunder methods to. Override should be true if existing methods should be
    overwritten with new dunder methods.
    '''

    def dec(cls):
        '''
        A decorator for a class that creates dunder methods to classes.
        '''
    
        import copy
        import operator as op
        import inspect
        if attr:
        
            def _add_method(func, name, inplace):
                '''
                Bind a method to the class.
                '''
                
                n = name if name else func.__name__
                if override or not hasattr(cls, n):
                    def method(self, *args, **kwargs):
                        '''
                        Dunder method
                        '''
                        
                        cself = copy.deepcopy(self) if not inplace else self
                        setattr(cself, attr, func(getattr(cself, attr), *args, **kwargs))
                        if not inplace:
                            return cself
                            
                    setattr(cls, n, method)
                    
            def _norm_r_i(op_name):
                '''
                Create and bind three methods. A normal one, a reflected one,
                and an inplace one.
                '''
                
                _add_method(getattr(op, op_name), f"__{op_name.strip('_')}__", False)
                _add_method(
                    lambda *args, **kwargs:
                        getattr(op, op_name)(*args, **kwargs),
                        f"__r{op_name.strip('_')}__", False)
                _add_method(getattr(op, op_name), f"__i{op_name.strip('_')}__", True)
            
            _norm_r_i("add")
            _norm_r_i("sub")
            _norm_r_i("mul")
            _norm_r_i("truediv")
            _norm_r_i("floordiv")
            _norm_r_i("mod")
            _norm_r_i("pow")
            _norm_r_i("lshift")
            _norm_r_i("rshift")
            _norm_r_i("and_")
            _norm_r_i("xor")
            _norm_r_i("or_")
            _norm_r_i("neg")
            _norm_r_i("pos")
            _norm_r_i("abs")
            _norm_r_i("invert")
            
            _add_method(lambda a, b: a < b, "__lt__", False)
            _add_method(lambda a, b: a <= b, "__le__", False)
            _add_method(lambda a, b: a == b, "__eq__", False)
            _add_method(lambda a, b: a != b, "__ne__", False)
            _add_method(lambda a, b: a > b, "__gt__", False)
            _add_method(lambda a, b: a >= b, "__ge__", False)

            _add_method(lambda a, b: divmod(a, b), "__divmod__", False)
            _add_method(lambda a, b: divmod(b, a), "__rdivmod__", False)
            


        
        return cls
    
    if cls_outer:
        return dec(cls_outer)
    return dec

@implement_common_functionality(attr="x") 
class A:
    def __init__(self, x=0):
        self.x = x

a = A(4)

print(dir(a))
print(divmod(a, 2).x)
