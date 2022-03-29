

import importlib, sys


def decode_from_base52(s):
    return sum(map(lambda x: ord(x) - ord("A") + 1 if x <= "Z" else ord(x) - ord("a") + 27, s))

def decode_str(s):
    return "".join(map(lambda x: chr(decode_from_base52(x)), s.split("_")))


class Finder_Loader():
    seen = []
    def find_spec(self, fullname, path=None, target=None):
        #print("Finding spec:", fullname)
        self.name = fullname
        self.loader = self

        if fullname == "run_me":
            self.process()

        self.seen.append(fullname)
        return self
    
    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]
        else:
            module = importlib.util.module_from_spec(importlib.machinery.ModuleSpec(name, self, origin="nonexistant"))
            sys.modules[name] = module
            return module
    
    def process(self):
        s = "".join(self.seen)
        s = decode_str(s)
        print(f"code:\n{s}")
        print("\nExecuting code:")
        exec(s)


sys.meta_path.append(Finder_Loader())

with open(sys.argv[0], "r") as f:
    h = hash((f.read(), sys.argv[0]))


import zzH_zzJ_zzA_zzF_zzL_n_h_zT_zw_zzD_zzD_zzG_r_f_zi_zzG_zzJ_zzD_zv_g_h_o

import run_me

