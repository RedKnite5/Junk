

a = [f for f in (exec("import importlib,sys", globals()), )]



class Finder_Loader():
    seen = []
    def find_spec(self, fullname, path=None, target=None):
        self.name = fullname
        self.loader = self
        self.seen.append(fullname)
        return self
    
    def load_module(self, name):
        print("Loading module:", name)
        if name in sys.modules:
            return sys.modules[name]
        else:
            module = importlib.util.module_from_spec(importlib.machinery.ModuleSpec(name, self, origin="nonexistant"))
            sys.modules[name] = module
            return module


#sys.meta_path.append(type("Finder", (object,), {"seen": [], "find_spec": classmethod(lambda cls, fullname, path=None, target=None: type("Loader", (object,), {"__init__": lambda self, fullname, path=None, finder=None: setattr(self, "loader", self) or setattr(self, "name", fullname) or setattr(self, "origin", "nonexistant") or setattr(self, "has_location", False) or setattr(self, "finder", finder), "load_module": lambda self, fullname: sys.modules[fullname] if self.finder.seen.append(fullname) or fullname in sys.modules else sys.modules.__setitem__(fullname, m := importlib.util.module_from_spec(importlib.machinery.ModuleSpec(fullname, self, origin="nonexistant"))) or m})(fullname, finder=cls))}))
sys.meta_path.append(Finder_Loader())

import my_module
your_module = __import__("your_module")

print(sys.meta_path[-1].seen)
#print(your_module.__loader__.finder.seen)
