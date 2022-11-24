from re import I


sub1=int(input("Please enter your marks"))
sub2=int(input("Please enter your marks"))
sub3=int(input("Please enter your marks"))


if sub1<33 and sub2 <33 and sub3 < 33 and ((sub1+sub2+sub3)/3) <40:
    print("You are fail")
else:
    print("You are pass")

