def spin(lst):
    start = 0
    for turn in lst:
        if turn.startswith("r"):
            start += 0.25
        elif turn.startswith("l"):
            start -= 0.25
    print(start)
spin("right, right, right, right, right, right, right, right")
# //////////////////////////////////////////////////////////////////////
def function(c):
    for i in range(len(c)):
        if c[i] != c[i][::-1]:
            print("It's not palindrome")
        else:
            print("It's palindrome")
function(['mom','madam','map'])
#/////////////////////////////////////////////////////////
nums = [4,0,-5,6,-3]
res = [var for var in nums if var > 0]
res2 = [var for var in nums if var < 0]
print(res, res2)
# /////////////////////////////////////////////////////
