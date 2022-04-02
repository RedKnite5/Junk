


def encode_to_base52(n):
    return "".join(map(lambda x: chr(ord("A") + x - 1 if x <= 26 else ord("a") + x - 27), [52] * (n // 52) + ([n % 52] if n % 52 else [])))

def encode_str(s):
    return "_".join(map(lambda x: encode_to_base52(ord(x)), s))

def decode_from_base52(s):
    return sum(map(lambda x: ord(x) - ord("A") + 1 if x <= "Z" else ord(x) - ord("a") + 27, s))

def decode_str(s):
    return "".join(map(lambda x: chr(decode_from_base52(x)), s.split("_")))



def test():
    assert encode_to_base52(1) == "A"
    assert encode_to_base52(2) == "B"
    assert encode_to_base52(25) == "Y"
    assert encode_to_base52(26) == "Z"
    assert encode_to_base52(27) == "a"
    assert encode_to_base52(28) == "b"
    assert encode_to_base52(51) == "y"
    assert encode_to_base52(52) == "z"
    assert encode_to_base52(53) == "zA"
    assert encode_to_base52(54) == "zB"
    assert encode_to_base52(78) == "zZ"
    assert encode_to_base52(79) == "za"

    assert decode_str(encode_str("abc")) == "abc"
    assert decode_str(encode_str("print(\"Hello, World!\")")) == "print(\"Hello, World!\")"

    s = """
class A(object):
    def __init__(self):
        self.a = 1
"""
    assert decode_str(encode_str(s)) == s

    s = 'ċŌÐêãĔĬēàÌãĘÊùøąÊõĄÿÙħûĖ»æÞÃ¹ÎøÅ¿ÍĂĔā½úÂÕÛÌÎØ·ð¬ÌúýÎãÚĆîÞ«ÔďèĂ¯Ñü«ðÓûČÂđÀÈ¾ÒÂòÝÃ£Ö¸È±ÌÕĠíâ¼ď¶´ÇúöĠąĀºÃ·®¬©·Ā¦Ĝâ'
    assert decode_str(encode_str(s)) == s

test()


s = encode_str("import zzH_zzJ_zzA_zzF_zzL_n_h_zT_zw_zzD_zzD_zzG_r_f_zi_zzG_zzJ_zzD_zv_g_h_o;print(\"Done\")")
print(s)

