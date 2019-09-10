def computepay(h,r):
    return hrs , rate
    pass
h = input("Enter hour:")
r = input("enter rate:")
try:
 hrs = float(h)
 rate = float(r)
 computepay(h,r)
 if hrs > 40:
    hr = hrs - 40
    r = rate * 1.5
    z = hr * r
    z2 = 40 * rate
    z3 = z2 + z
    print(z3)
 else:
    done = hrs * rate
    print(done)
except:
    print("please enter a numeric input")
