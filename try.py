def f(a,b):
    try:
        c=int(a)
        b=c+"A"
        print(b)
    except TypeError:
        print("T")
    finally:
        print("IF")
try:
    f('R',13)
except ValueError:
    print("V")
finally:
    print("OF")