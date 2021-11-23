import ctypes

def deref(addr, typ):
    return ctypes.cast(addr, ctypes.POINTER(typ))


def swap(a, b):
	bytes_a = a.to_bytes(1, "big")
	deref(id(a), ctypes.c_int)[6] = b
	deref(id(b), ctypes.c_char)[24] = bytes_a




swap(29, 100)

x = 29
print("x=29")
print(f"{x * 2=}")
print(f"{20 + 9=}")
print(f"{1_000_000=}")
print(f"{50 * 2=}")

swap(29, 100)

x = 29
print("x=29")
print(f"{x * 2=}")
print(f"{20 + 9=}")
print(f"{100=}")
print(f"{50 * 2=}")

