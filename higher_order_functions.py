




def compose(func, count, *args, **kwargs):
    ans = args[0]
    for i in range(count):
        ans = func(ans, *args[1:], **kwargs)
    return ans


def tests():
    def func(x, inc=1):
        return x+inc
    
    
    print(compose(func, 5, 0))


if __name__ == "__main__":
    tests()