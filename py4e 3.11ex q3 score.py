s = input("Please Enter Score :")
score = float(s)
if score < 0.0 or score > 1.0:
    print("Bad Score")
    pass
else:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("c")
    elif score >= 0.5:
        print("D")
    elif score < 0.6:
        print("F")
