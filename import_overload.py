# import_overload.py

import builtins
import importlib


old_imp = builtins.__import__

def my_import(*args, **kwargs):
	if args[0] == "foo":
		return "Foo me"
	else:
		return old_imp(*args, **kwargs)

builtins.__import__ = my_import

import foo
#print(type(foo))

import sys


class Finder(object):
	def find_module(self, fullname, path=None):
		if fullname == "bar":
			return Loader()
		return None


class Loader(object):
	def load_module(self, fullname):
			if fullname in sys.modules:
				return sys.modules[fullname]
			spec = importlib.machinery.ModuleSpec(fullname, None)
			mod = importlib.util.module_from_spec(spec)
			mod.__loader__ = self
			sys.modules[fullname] = mod
			
			mod.__file__ = "Naw"
			code = "print('bar you')\nx=5"
			exec(code, mod.__dict__)

			return mod
	
	def create_module(self, spec):
		return None



sys.meta_path = [Finder()]

import os

import bar
print(bar.x)


	
