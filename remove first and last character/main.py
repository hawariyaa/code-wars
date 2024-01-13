# remove the first and last character from a given string
def remove_char(s):
    #your code here
    new = []
    for i in range(len(s)):
        if i == 0:
            pass
        elif i == len(s) - 1:
            pass
        else:
            new.append(s[i])
    return "".join(new)

s = "hawi"
answer = remove_char(s)
print(answer)