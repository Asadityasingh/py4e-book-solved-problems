count = 0
sum = 0
avg = 0
while True:
#    try:
        f = input("enter file name  ::")
        x = open(f)
        for line in x:
            if line.startswith ('X-DSPAM-Confidence:'):
                str = (line)
                count += 1
                aq = (str[19:])
                z = float(aq)
        #        count += 1
                sum += z
                avg = sum / count
                print(avg)
                #print(sum)
#    except:
#        print("not done")
