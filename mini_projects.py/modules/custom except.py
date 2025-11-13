class Myecxept(Exception):
    pass

try:
    n = int(input("Val: "))
    if n<0:
        raise Myecxept("No neg val")
    else:
        print("Valid")
except Myecxept as e:
    print(e)

except ValueError:
    print("Diff dt")
else:
    print("Err")