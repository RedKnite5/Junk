
import importlib, sys


def decode_from_base52(s):
    return sum(map(lambda x: ord(x) - ord("A") + 1 if x <= "Z" else ord(x) - ord("a") + 27, s))

def decode_str(s):
    return "".join(map(lambda x: chr(decode_from_base52(x)), s.split("_")))


class Finder_Loader():
    def find_spec(self, fullname, path=None, target=None):
        #print("Finding spec:", fullname)
        self.name = fullname
        self.loader = self
        return self
    
    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]
        else:
            module = importlib.util.module_from_spec(importlib.machinery.ModuleSpec(name, self, origin="nonexistant"))
            exec(self.process(), module.__dict__)

            sys.modules[name] = module
            return module
    
    def process(self):
        s = "".join(self.name)
        s = decode_str(s)
        return s


sys.meta_path.append(Finder_Loader())

with open(sys.argv[0], "r") as f:
    h = hash((f.read(), sys.argv[0]))


import zzA_zzE_zzH_zzG_zzJ_zzL_f_zzR_zzR_zT_zq_zzR_zzR_zV_zq_zzR_zzR_zM_zq_zzR_zzR_zR_zq_zzR_zzR_zX_zq_zzF_zq_zz_zq_zzR_zf_zq_zzR_zzO_zq_zzR_zzR_zP_zq_zzR_zzR_zP_zq_zzR_zzR_zS_zq_zzJ_zq_zx_zq_zzR_zzA_zq_zzR_zzR_zS_zq_zzR_zzR_zV_zq_zzR_zzR_zP_zq_zzR_zzN_zq_zy_zq_zz_zq_zzG_zG_zzH_zzJ_zzA_zzF_zzL_n_h_zP_zzG_zzF_zw_h_o
