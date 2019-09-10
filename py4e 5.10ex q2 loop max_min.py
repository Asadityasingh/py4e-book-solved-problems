largest = None
smallest = None
while True:
    try:
        x = input('Enter Number : ')
        if  x == 'done':
            break
        y = float(x)
        if largest is None or y > largest :
            largest = y
        elif smallest is None or y < smallest:
            smallest = y
    except:
        print("Bad Data")
print(largest , smallest)
#source:creativity
