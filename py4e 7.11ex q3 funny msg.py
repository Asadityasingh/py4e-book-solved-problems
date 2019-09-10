f = input('enter file name :')
if f == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhand = open(f)
except:
    print('file cannot be open: ', f)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print ('there is' ,count, "lines in this file called", f)
