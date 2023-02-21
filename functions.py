name = input("Enter your name:- ")
age =  int(input("Enter your age:- "))

def vote_eligibility():
    if age >= 18:
        return 1
    else :
        return 0

ans = vote_eligibility()
if ans == 1:
    print("Congratulations! ",name," you're eligible to vote because your age is ",age)
else:
    print("Sorry! ", name ," you're not eligible to vote because your age is ", age)