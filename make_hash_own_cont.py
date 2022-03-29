


def encode_to_base52(n):
    return "".join(map(lambda x: chr(ord("A") + x - 1 if x < 26 else ord("a") + x - 27 ),  [52] *  (n // 52) + [n % 52]))

def encode_str(s):
    return "_".join(map(lambda x: encode_to_base52(ord(x)), s))

def decode_from_base52(s):
    return sum(map(lambda x: ord(x) - ord("A") + 1 if x <= "Z" else ord(x) - ord("a") + 27, s))

def decode_str(s):
    return "".join(map(lambda x: chr(decode_from_base52(x)), s.split("_")))




s = encode_str("print(\"Hello, World!\")")
print(s)
