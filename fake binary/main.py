# fake binary
# if the number is less than 5 put 0 and, 5 and above put 1
def fake_bin(x):
    stri = []
    for i in x:
        if int(i) < 5:
            stri.append('0')
        else:
            stri.append('1')
    return "".join(stri)
# the join changes an array(list) or tuples to a string and the "" is a quotation, what we put inside will
# appear inbetween each character in the string, so in the above case we just left it empty
x = "23456788"
answer = fake_bin(x)
print(answer)