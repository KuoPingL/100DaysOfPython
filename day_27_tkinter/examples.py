def get_key(**kw):
    print(kw)


def get_tuple(*args):
    print(args)


get_key(a="1", b="2", c=3, d=123.4)

get_tuple(1, 2, 3, "a", "10", 124.4)
# get_tuple(1)

