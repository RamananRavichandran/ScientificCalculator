"""program"""

def cube_root(n_value):
    """function"""
    v=int(n_value)
    try:

        if v > 0:
            print(v**(1/3))
            return v**(1/3)

        elif v < 0:
            print(-(-v)**(1/3))
            return -(-v)**(1/3)


    except TypeError:
        res = "enter only numbers"
        return res
