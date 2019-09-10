count = 0
sum = 0
avg = 0

while True:
    try:
        x = input('Enter Number : ')
        if  x == 'done':
            break
        y = float(x)
        count += 1
        sum += y
        avg = count / sum
    except:
        print("Bad Data")
print(count, sum, avg)
#scorce: https://trinket.io/python/79b285a420
