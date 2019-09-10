def computegrade(S):
    return Score
    pass
S = input("Please Enter Score :")
Score = float(S)
#S = Score
computegrade(S)
if Score < 0.0 or Score > 1.0:
    print("Bad Score")
    pass
else:
    if Score >= 0.9:
        print("A")
    elif Score >= 0.8:
        print("B")
    elif Score >= 0.7:
        print("c")
    elif Score >= 0.5:
        print("D")
    elif Score < 0.6:
        print("F")
