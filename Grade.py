#The Grade Program
def result(H,A,F):
    answer = ((H/25)*100) + ((A/50)*100) + ((F/100)*100)
    #weighting = ((H*0.25), (A*0.35), (F*0.40))
    score = round(answer/3)
    Studentname = input("Enter your name: ")
    if score >= 80:
        print("You scored:",score,"% You've achieved grade: A*, Excellent")
    elif score >= 70:
        print("You scored:",score,"% You've achieved grade: A, Awesome")
    elif score >= 60:
        print("You scored:",score,"% You've achieved grade: B, Great")
    elif score >= 50:
        print("You scored:",score,"% You've achieved grade: C, Good")
    elif score >= 40:
        print("You scored:",score,"% You've achieved grade: D, Pass")
    elif score >= 35:
        print("You scored:",score,"% You've achieved grade: E Pass")
    else:
        print("You scored:",score,"% You've achieved grade: F, 'UC'")
    #return score
mark = result(15,39,85)

#weighting
def weighting(H,A,F):
    w = (round((H/25)*25), round((A/50)*35), round((F/100)*40))
    return w

b = weighting(15,39,85)
print(b)

#weighting(24,45,95)
#print(mark)
#print(answer2)
